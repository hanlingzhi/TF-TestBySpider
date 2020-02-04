__author__ = 'hanlingzhi'

'''
create_date: 2019.12.5
usage: global vars
'''

global_dict = {}


def init():  # 初始化
    global global_dict
    if len(global_dict > 0):
        raise Exception("Global variables have been init ...")
    global_dict = {}


def set_value(key, value):
    """ Define a global variable """
    global global_dict
    global_dict[key] = value


def is_exist(key):
    """ global variable exists """
    global global_dict
    return key in global_dict


def get_value(key, def_value=None):
    """ If it does not exist, return the default value """
    global global_dict
    try:
        return global_dict[key]
    except KeyError:
        return def_value
