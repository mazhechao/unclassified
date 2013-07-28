# -*- coding: UTF-8 -*-
import httplib
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

city = ["%E5%8D%97%E4%BA%AC", # 南京
		"%E6%97%A0%E9%94%A1", # 无锡
		"%e8%8b%8f%e5%b7%9e", # 苏州
		"%e5%b8%b8%e5%b7%9e", # 常州
		"%e9%95%87%e6%b1%9f", # 镇江
		"%e5%8d%97%e9%80%9a", # 南通
		"%e6%89%ac%e5%b7%9e", # 扬州
		"%e6%b7%ae%e5%ae%89", # 淮安
		"%e7%9b%90%e5%9f%8e", # 盐城
		"%e6%b3%b0%e5%b7%9e", # 泰州
		"%e5%ae%bf%e8%bf%81", # 宿迁
		"%e8%bf%9e%e4%ba%91%e6%b8%af", # 连云港
		"%e5%be%90%e5%b7%9e"] #徐州

host = "common.jiangsu.sina.com.cn"
url = "/z/2013hope/getList.php?city=" + city[0] + "&page="
for i in range(1,20):
	conn = httplib.HTTPConnection(host)
	conn.request("GET", url+repr(i))
	res = conn.getresponse()
	#print res.read()
	stulist = json.loads(res.read()[1:-1])["list"]
	#print stulist
	for stu in stulist:
		if stu['gender'] == u'\u7537' and int(stu['score']) >= 328:
		#if stu['gender'] == u'\u7537':
			print stu['stuName'],stu['gender'],stu['schInfo'],stu['score'],stu['reason'],"\n"

