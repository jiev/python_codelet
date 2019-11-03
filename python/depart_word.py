import jieba

while True:
	aa = raw_input('>')
	words = jieba.cut(aa)

	for w in words:
		print w


