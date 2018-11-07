
#!/usr/bin/env python
#-*- coding: utf-8 -*-

__version__="1.0.0" ## It just functions.
__author__="Ashton"

"""
This script grabs data from dailyfx every X seconds.
This program is only set to run 25 iterations and update
every 3 seconds (to be as accurate as possible.)
"""

## Imports
import sys
import urllib
import json
import datetime
import time

##
class fxcm_data():
    """This class is for grabbing and displaying the data."""
    def get_url(self):
        the_time = datetime.datetime.now()
        callback = the_time.strftime("%Y%m%d%H%M%S")
        optimized_time = the_time.strftime("%Y/%m/%d - %H:%M:%S")

        ## CHG CURRENCY TYPES HERE
        curr_one = "EURUSD" # default " EURUSD"
        curr_two = "USDCAD" # default = "USDCAD"
        url =  "http://ratesjson.fxcm.com/DataDisplayer?symbols={},{}&callback=jsonCallback=".format(curr_one, curr_two)+ str(callback)
        exchange_data = urllib.urlopen(url)

        ## Parse the strings
        self.parse_strings(curr_one, curr_two, exchange_data, optimized_time)



    def parse_strings(self, X, Y, strings_to_parse, optimized_time):
        parsed_string = strings_to_parse.read().split("\"")

        ## Parses the first currency.
        curr_one_bid = parsed_string[9]
        curr_one_ask = parsed_string[13]
        curr_one_spread = parsed_string[17]

        curr_two_bid = parsed_string[29]
        curr_two_ask = parsed_string[33]
        curr_two_spread = parsed_string[37]

        post_curr_one = '{} | Bid: {} | Ask: {} | Spread: {}'.format(Y, curr_one_bid, curr_one_ask, curr_one_spread)
        post_curr_two = '{} | Bid: {} | Ask: {} | Spread: {}'.format(X, curr_two_bid, curr_two_ask, curr_two_spread)

        self.set_display(optimized_time, post_curr_one, post_curr_two)


    def set_display(self, optimized_time, post_curr_one, post_curr_two):
        print('\t[Data as of : {} ]\n'.format(optimized_time))
        print('\t\t{}\n'.format(post_curr_one))
        print('\t\t{}'.format(post_curr_two))
        



    def clear(self):
        import os
        os.system('printf \033c"')
        os.system('clear')




if __name__ == '__main__':
    for x in range(0, 25):
        data = fxcm_data()
        data.clear()
        print(data.get_url())
        time.sleep(3)
