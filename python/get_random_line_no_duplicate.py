#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import unicodedata
import random

# 格式：  python get_random.py 输入文件名  输出文件名  抽取个数n
# 效果说明 ： 从输入文件中随机抽取  n  行 ，并将结果写入输出文件中。 且抽取的行不重复

if __name__ == '__main__':
	file_in = open(sys.argv[1],'r')
	file_out = open(sys.argv[2],'w')

	count = int(sys.argv[3])

	choose_set = set()

	lines =  file_in.readlines()
	line_count = len(lines)

	if count >= line_count:
		print 'error ! choose count larger than file count .'
		sys.exit()

	i = 0
	while i < count:
		rand = random.randint(0,line_count)
		while rand in choose_set:
			rand = random.randint(0,line_count)
		choose_set.add(rand)
		try:
			file_out.write(lines[rand])
		except:
			print rand
			continue

		i = i + 1


	file_out.close()
	file_in.close()