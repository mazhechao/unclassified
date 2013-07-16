# -*- coding: UTF-8 -*-
import httplib
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

city = ["%E5%8D%97%E4%BA%AC","%E6%97%A0%E9%94%A1"]

host = "common.jiangsu.sina.com.cn"
url = "/z/2013hope/getList.php?city=" + city[1] + "&page="
for i in range(1,20):
	conn = httplib.HTTPConnection(host)
	conn.request("GET", url+repr(i))
	res = conn.getresponse()
	#print res.read()
	stulist = json.read(res.read()[1:-1])["list"]
	#print stulist
	for stu in stulist:
		if stu['gender'] == u'\u7537' and int(stu['score']) >= 328:
		#if stu['gender'] == u'\u7537':
			print stu['stuName'],stu['gender'],stu['schInfo'],stu['score'],stu['reason'],"\n"

