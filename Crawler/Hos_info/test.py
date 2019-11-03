#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import psycopg2
import urllib

processed_urls = []
f2 = open('test.txt','w')
count = 0 
f = open('hos_info.txt','r')
recorded_names = []
for line in f:
	recorded_names.append(line.split(u'\t')[0])
	#count += 1
	#if count %1000 ==0:
		#print line.split(u'\t')[0]

print len(recorded_names)

url_connection = psycopg2.connect('dbname=hos_info_db user=postgres password=new_psd')
cursor = url_connection.cursor()
cursor.execute("SELECT * FROM processed_url")

contents = cursor.fetchall()
for content in contents:
	if content[0].endswith('E9%99%A2'):
		hos_name = urllib.unquote(content[0].split('/')[-1])
		if not hos_name in recorded_names:
			cursor.execute("INSERT INTO processing_url (url) VALUES('"+content[0]+"')")
			cursor.execute("DELETE  FROM processed_url WHERE url='"+content[0]+"'")
			
url_connection.commit()

print count
print len(contents)

f.close()
cursor.close()

