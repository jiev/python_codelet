#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 对一列数据中，出现的词及该词的次数进行统计。
# 例如：该列内容为 “AABC” ，则输出为  A 2   B 1   C 1

if __name__ == '__main__':
	file_in = open(sys.argv[1],'r')
	file_out = open(sys.argv[2],'w')

	all_map = dict()

	count = 0
	for line in file_in:
		count += 1
		if count % 10000 == 0 :
			print count

		line = line.strip();
		if len(line) == 0 :
			continue

		try:
			if all_map.has_key(line):
				all_map[line] = all_map[line] + 1
			else:
				all_map[line ] = 1
		except:
			print 'something wrong'
			continue

	keys = all_map.keys()
	keys.sort()
	keys.reverse()

	for k in keys:
		file_out.write(k+ '\t' +str(all_map[k]) + '\n')



	file_in.close()
	file_out.close()

