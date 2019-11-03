#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#
# 或取文本行中包含指定文本的指定列。
# 输入格式 ：  python get_string_in_line.py infile_name outfile_name string_to_find  colume
# 如果不指定 colume ，则获取整行内容
# 多个 string_to_find 用 '|'分隔
#

if __name__ == '__main__':
	file_in = open(sys.argv[1],'r')
	file_out = open(sys.argv[2],'w')
	colume = -1
	if len(sys.argv) > 4:
		colume = int(sys.argv[4])

	to_find = sys.argv[3].split('|')

	for line in file_in:
		for item in to_find:
			if item in line:
				if colume != -1:
					file_out.write(line.split('\t')[colume] + '\n')
				else:
					file_out.write(line)
				break
		

	file_in.close()
	file_out.close()


