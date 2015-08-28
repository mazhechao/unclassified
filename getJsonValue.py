#!/usr/bin/python

import sys
import urllib
import json

def getJsonValue(url, nodeName):
    #print url, nodeName
    try:
        res = urllib.urlopen(url)
        jsonObj = json.loads(res.read())
        items = nodeName.split('/')
        items[0] = jsonObj
        print reduce(lambda x, y:x.__getitem__(y) if not isinstance(x, list) else x[int(y)], tuple(items))
    except:
        print -1


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(1)
    api = sys.argv[1]
    node = sys.argv[2]
    getJsonValue(api, node)
