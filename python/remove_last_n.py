# -*- coding: UTF-8 -*-

chineseMarkSet = set([u"。", u"，" ,u"（", u"）" ,u"、", u"：" ,u"？",u"；",])

fo = open("temp_line_out.txt","w")
for line in open("temp_line","r"):
	line = line.rstrip()
	if len(line) > 0:
		res = ""
		last_c = None
		for i,c in enumerate(line):
			if last_c in chineseMarkSet:     
				if c == " ":
					# 中文符号后面的空格去掉
					continue

			res += c
			last_c = c
		fo.write(res)
	else:
		fo.write("\n")

fo.close()

