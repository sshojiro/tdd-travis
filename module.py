# coding=utf-8


# http://uxmilk.jp/8662
# http://uxmilk.jp/41416
import re


def parse_nums(string):
    pttr = re.compile('[-\ ]?0\.\d{1,5}')
    return pttr.findall(string)


def trim_symbol(string):
    ret = ''.join(re.sub('[\[\]\(\)\-]', ' ', string))
    ret = re.sub('( ){2,}', ' ', ret)
    return re.sub('^ ', '', ret)