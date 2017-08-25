#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import optparse
from urlparse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS
import socks
import socket 


socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, "127.0.0.1", 9050, True)
socket.socket = socks.socksocket


def findImages(url):
    print ('[+]=> procurando imagens na url => ' + url)
    urlContent = urllib2.urlopen(url).read()
    try:
        urlContent = urllib2.urlopen(url).read()
    except urllib2.HTTPError, e:
        print e.code
    except urllib2.URLError, e:
        print e.args
    soup = BeautifulSoup(urlContent, 'html.parser')
    imgTags = soup.findAll('img')
    return imgTags
    print("saida")


def downloadImage(imgTag):
    try:
        print ('[+]=> baixando imagen ...')
        imgSrc = imgTag['src']
        imgContent = urllib2.urlopen(imgSrc).read()
        imgFileName = basename(urlsplit(imgSrc)[2])
        imgFile = open(imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except:
        return ''


def testForExif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()
        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print ('[*] ' + imgFileName + \
                 ' contains GPS MetaData')
    except:
        pass


def main():
    dsa = open("link1.txt", "r+")
    for url in dsa: 
    	if url == None:
        	print ("saida")
        	exit(0)
    	else:
        	imgTags = findImages(url)
        	for imgTag in imgTags:
            		imgFileName = downloadImage(imgTag)
            		testForExif(imgFileName)


if __name__ == '__main__':
    main()
