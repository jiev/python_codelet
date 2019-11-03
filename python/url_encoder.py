#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("gb2312")
import urllib

# 将 下载的 log 文件中的 URL 下载先来解析。

if __name__ == '__main__':
	file_in = open(sys.argv[1],'r')
	file_out = open(sys.argv[2],'w')

	count = 0
	for line in file_in:

		count += 1
		if count % 10000 == 0:
			print count

		segs = line.split('what=keyword:')
		if len(segs) > 1:
			keyword = segs[1].split('&')[0]
			if len(keyword) < 1:
				continue

		url_segs = line.strip().split('=')
		if len(url_segs) < 2:
			continue

		url = url_segs[0]
		for item in url_segs[1:]:
			item_to_quote = item.split('&',1)
			if len(item_to_quote) > 1:
				item = urllib.quote(item_to_quote[0]) + '&' + item_to_quote[1]
			else:
				item =  urllib.quote(item_to_quote[0])

			url = url + '=' + item

		if( ('keyword' in url) and (not ' ' in url) ):
			file_out.write(url + '\n')


	file_out.close()
	file_in.close()
