# coding=utf-8

import sys
import time
__author__ = 'hanlingzhi'

'''
:create_date:
    2017.7.26
:usage:
    print format util
'''


class PrintFormatUtil:

    def __init__(self):
        pass

    @staticmethod
    def print_title(text, is_color=False):
        if is_color:
            print("%s%s%s" % ('\033[32m' + '=' * 25, text, '=' * 25 + '\033[0m'))
        else:
            print("%s%s%s" % ('=' * 25, text, '=' * 25))

    @staticmethod
    def print_line(text, is_color=False):
        if is_color:
            print("%s [%s] - %s%s" % ('\033[32m* ', time.asctime(time.localtime(time.time())), text, '\033[0m'))
        else:
            print("%s [%s] - %s" % ('* [SPIDER]', time.asctime(time.localtime(time.time())), text))

    @staticmethod
    def print_success(text, is_color=False):
        if is_color:
            print("%s [%s] [%s] - %s%s" % ('\033[32m [SPIDER] ', time.asctime(time.localtime(time.time())), 'SUCCESS',
                                          text, '\033[0m'))
        else:
            print("%s [%s] [%s] - %s" % ('* [SPIDER]', time.asctime(time.localtime(time.time())), 'SUCCESS', text))

    @staticmethod
    def print_error(text, is_color=False):
        if is_color:
            print("%s [%s] [%s] - %s%s" % ('\033[32m [SPIDER] ', time.asctime(time.localtime(time.time())), 'ERROR', text
                                          , '\033[0m'))
        else:
            print("%s [%s] [%s] - %s" % ('* [SPIDER]', time.asctime(time.localtime(time.time())), 'ERROR', text))

    @staticmethod
    def print_multi_line(text):
        for line in str(text).split("\n"):
            if line != "":
                PrintFormatUtil.print_line(line)

    @staticmethod
    def format_print_not_line(shell_string):
        sys.stdout.write(shell_string)
        sys.stdout.flush()
