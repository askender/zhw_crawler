#  -*- coding: utf-8-*-
import os
import sys


def filter_tags(htmlstr):
    import re
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)
    re_script = re.compile(
        '<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)
    re_style = re.compile(
        '<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)
    re_br = re.compile('<br\s*?/?>')
    re_h = re.compile('</?\w+[^>]*>')
    re_comment = re.compile('<!--[^>]*-->')
    s = re_cdata.sub('', htmlstr)
    s = re_script.sub('', s)
    s = re_style.sub('', s)
    s = re_h.sub('', s)
    s = re_comment.sub('', s)

    blank_line = re.compile('\n+')
    blank_r = re.compile('\r+')
    s = blank_line.sub('', s)
    s = blank_r.sub('', s)
    s = re_br.sub('', s)
    return s


def import_class(import_str):
    mod_str, _sep, class_str = import_str.rpartition('.')
    try:
        __import__(mod_str)
        return getattr(sys.modules[mod_str], class_str)
    except (ImportError, ValueError, AttributeError) as e:
        print(e)
        raise ImportError


def get_id_range(path):
    id_range = []
    if os.path.isfile(path):
        with open(path, 'r') as fp:
            for eachline in fp:
                if not eachline.startswith('#'):
                    shopid = eachline.replace('\r', '').replace('\n', '')
                    if shopid.isdigit():
                        id_range.append(int(shopid))
    return id_range
