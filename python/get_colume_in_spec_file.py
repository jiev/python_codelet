#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 从文件中换取制定列。
# 使用方法：
# 	python get_colume_in_spec_file.py  file_in_name file_out_name  用逗号分隔的要提取的行号
#
if __name__ == '__main__':
	file_in = open(sys.argv[1],'r')
	file_out = open(sys.argv[2],'w')

	columes = [int(x) for x in sys.argv[3].split(',')]

	for line in file_in:
		contents = line.strip().split('\t')
		if len(contents) < 2:
			continue

		write_content = ''
		try:
			for colume in columes:
				write_content += contents[colume] + '\t'

			file_out.write(write_content.rstrip('\t')+'\n')
		except:
			print line.decode('utf-8'),
			continue

	file_in.close()
	file_out.close()


