# ----------------------------------
# Ralsei/utils/converter
# Fixed by Infinidoge, created by David Bain (originally from pycurrency, created by Davin Bain
# ----------------------------------
# Echos the message the user send as the bot, subtracting the command itself. ([prefix]print)
# ----------------------------------


import json
import urllib
import re


class Converter:
    """ A currency converter class """
    def __init__(self, amount, from_cur, to_cur, rates={}):
        self.amount = amount
        self.from_cur = from_cur
        self.to_cur = to_cur
        self._rates = rates
        self._ratio = self.update()
        self.url = None
        self.query = None

    def ratio(self):
        return self._ratio

    def update(self):

        fromto = "%s-%s" % (self.from_cur, self.to_cur)
        cur_ratio = {}

        if fromto in self._rates.keys():
            result = self._rates[fromto] * self.amount
            cur_ratio['from'] = self.amount
            cur_ratio['to'] = result

        else:
            self.query = {"amount": self.amount,
                          "from": self.from_cur,
                          "to": self.to_cur,
                          "eq": '%3D%3F'}  # the %3D%3F is equivalent to ?=

            self.url = "http://www.google.com/ig/calculator?hl=en&q=%(amount)s%(from)s%(eq)s%(to)s" % self.query

            request = urllib.urlopen(self.url)
            raw_data = request.read()
            raw_data = raw_data.replace('\xa0','')
            j = self.sanitize(raw_data)
            data = json.loads(j)
            lhs = float(data['lhs'].split(" ")[0])
            rhs = float(data['rhs'].split(" ")[0])
            cur_ratio['from'] = lhs
            cur_ratio['to'] = rhs
            self._rates[fromto] = rhs / self.amount

        self._ratio = cur_ratio

        return cur_ratio

    def result(self):

        return self._ratio['to']
      
    def add_rate(self, fromto, value):
        self._rates[fromto] = value

    def rates(self):
        return self._rates

    def sanitize(self, raw_data):
        """ cleans up json that doesn't use double quotes 
           for its keys """
        j = raw_data
        # The json returned from this service is badly formatted
        # json.loads expects well formed json
        # with keys that have double quotes
        # e.g. {"good":"json","uses":"doublequotes"}
        # The regular expressions
        # below are used to clean up the
        # returned object and make it proper json
        # borrowed from http://stackoverflow.com/questions/4033633/handling-lazy-json-in-python-expecting-property-name

        j = re.sub(r"{\s*(\w)", r'{"\1', j)
        j = re.sub(r",\s*(\w)", r',"\1', j)
        j = re.sub(r"(\w):", r'\1":', j)

        return j


def convert(amount, from_cur, to_cur):
    return Converter(amount, from_cur, to_cur).result()
