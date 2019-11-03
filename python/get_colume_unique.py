#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 取列中出现的去重之后的唯一值。如果没有指定列，则取不同的行

if __name__ == '__main__':
	file_in = open(sys.argv[1],'r')
	file_out = open(sys.argv[2],'w')

	colume = -1
	if len(sys.argv) == 4:
		colume = int(sys.argv[3])

	line_set = set()
	for line in file_in:
		if colume == -1 :
			line_set.add(line)
		else:
			line_set.add(line.rstrip().split('\t')[colume])

	for key in line_set:
		if colume == -1:
			file_out.write(key)
		else:
			file_out.write(key + '\n')


	file_out.close()
	file_in.close()


