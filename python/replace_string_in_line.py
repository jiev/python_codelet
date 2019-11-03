#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 输入参数： in_file  out_file string_to_replace  string_replace_to

if __name__ == '__main__':
	file_in = open(sys.argv[1],'r')
	file_out = open(sys.argv[2],'w')

	to_replace = sys.argv[3]
	replace_to = sys.argv[4]

	for line in file_in:
		to_write = replace_to.join(line.split(to_replace))
		file_out.write(to_write)
		

	file_in.close()
	file_out.close()


