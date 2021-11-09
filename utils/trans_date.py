# -*- coding: utf-8 -*-
from datetime import datetime
import time

def convert2timestamp(tm):
    """ 转化为时间戳 timestamp """
    if isinstance(tm, datetime):
        return tm.timestamp()
    elif isinstance(tm, (int, float)):
        return float(tm)
    elif isinstance(tm, str):
        try:
            return float(tm)
        except ValueError:
            try:
                #rfc3339 格式
                return datetime.strptime(tm,
                                '%Y-%m-%dT%H:%M:%S+08:00').timestamp()
            except ValueError:
                return 0
    return 0


def try_parsing_datetime(text):
    for fmt in ('%Y-%m-%d', '%Y-%m-%d %H:%M:%S', '%Y.%m.%d', '%Y/%m/%d',
                '%Y-%m-%dT%H:%M:%S+08:00'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass
    raise ValueError(f'no valid date format found for {text}')


def utc2local(utc_st):
    """ UTC时间转本地时间（+ 8: 00）"""
    now_stamp = time.time()
    local_time = datetime.fromtimestamp(now_stamp)
    utc_time = datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st


def local2utc(local_st):
    """ 本地时间转UTC时间（- 8: 00）"""
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.utcfromtimestamp(time_struct)
    return utc_st
