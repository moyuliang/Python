# -*- coding: utf-8 -*-
import logging
import re
import urllib.request

'''爬取网页的图片'''

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler

handler = logging.FileHandler('..\..\\log\download_img.log')
handler.setLevel(logging.DEBUG)

# Create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)

# 获取传入的url中包含的图片的url
def get_img_url(url):
    logger.info('Start function get_url()')

    buf = urllib.request.urlopen(url).read().decode('utf-8')

    listurl = re.findall(r'src="//img.+\.jpg', buf)

    logger.debug('listurl = %s' % listurl)

    imglist = map(lambda s: 'http:' + s[5:], listurl)

    logger.debug('imglist = %s' % imglist)

    logger.info('End function get_url()')

    return imglist

# 根据传入的url列表下载图片
def download_img(imglist):

    logger.info('Start function download_img()')

    i = 1
    for url in imglist:
        f = open('..\..\\jpg\\' + str(i) + '.jpg', 'wb+')
        buf = urllib.request.urlopen(url).read()
        f.write(buf)
        logger.debug('%s.jpg，url= %s' % (i, url))
        i += 1

    logger.info('End function download_img()')

if __name__ == '__main__':
    imglist = get_img_url('http://www.imooc.com/course/list')
    download_img(imglist)