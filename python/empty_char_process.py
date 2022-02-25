# -*- coding: UTF-8 -*-


def is_alpha(a):
	return a.upper() != a.lower()

def is_chinese(uchar):
	"""判断一个unicode是否是汉字"""
	if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
		return True
	else:
		return False

fo = open("temp_out_eng.txt","w")
for line in open("temp.txt","r"):
	line = line.rstrip()
	if len(line) > 0:
		res = ""
		last_c = None
		for i,c in enumerate(line):
			if c == u" ":     
				# 前一个是汉字，后一个是字母的 空格 ,保留
				if last_c is not None and (not is_alpha(last_c)):
					if i < (len(line) - 1) and is_alpha(line[i + 1]):
						res += c

				# 前一个是字母，后一个是汉字的 空格 ,保留
				if last_c is not None and (is_alpha(last_c)):
					if i < (len(line) - 1) and is_chinese(line[i + 1]):
						res += c

				# 其他空格不要
				continue

			res += c
			last_c = c

		res += "\n"
		fo.write(res)
	else:
		fo.write("\n")

fo.close()
