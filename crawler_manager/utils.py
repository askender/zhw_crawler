#  -*- coding: utf-8-*-


import sys
sys.path.append('../')


def get_job_num(spider):
    import_str = 'zhw_crawler.conf.%s_conf.ID_RANGE' % spider
    id_range = import_class(import_str)
    num = len(id_range) if len(id_range) != 2 else id_range[1] - id_range[0]
    return num


def import_class(import_str):
    mod_str, _sep, class_str = import_str.rpartition('.')
    try:
        __import__(mod_str)
        return getattr(sys.modules[mod_str], class_str)
    except (ImportError, ValueError, AttributeError) as e:
        print(e)
        raise ImportError
