# -*- coding:utf-8 -*-
"""
沪深F10数据接口
Created on 2015/11/26
@author: TsaiYee
@group : moneye.net
@contact: yee.tsai@gmail.com
"""
import pandas as pd
from tushare.stock import cons as ct
import lxml.html
from lxml import etree
import re
from pandas.compat import StringIO

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request


def get_f10_fh(year=None, code=None, retry_count=3):
    """
    获取个股分红数据
    Parameters
    ------
    year:string
              年份 format: YYYY 为空时默认为所有年份
    code:string
              股票代码 e.g. 600848 为空时默认为所有股票
    retry_count : int, 默认 3
              如遇网络等问题重复执行的次数
    pause : int, 默认 0
             重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    return
    -------
    DataFrame
        属性:股票代码，股票名称， 公告日期， 分红年度， ， 成交量， 价格变动 ，涨跌幅，5日均价，10日均价，20日均价，5日均量，10日均量，20日均量，换手率
    """


