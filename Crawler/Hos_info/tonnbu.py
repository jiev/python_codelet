import psycopg2


start_urls = []

url = 'stupid'
url_connection = psycopg2.connect('dbname=hos_info_db user=postgres password=new_psd')
cursor = url_connection.cursor()
cursor.execute("INSERT INTO processing_url (url) VALUES('"+url+"')")
cursor.execute("SELECT * FROM processing_url")

contents = cursor.fetchall()
if len(contents  ) == 0:
	pass
else:
	for content in contents:
		start_urls.append(content[0])	

print '===========================================\n'+''.join(start_urls)+'\n==========================================='

cursor.close()
url_connection.commit()
