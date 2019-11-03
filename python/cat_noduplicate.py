#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import shutil
import os

# 将多个文件合并，出现在前面文件的，添加后面文件中的元素时不会再次加入。

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print u'输入的文件数量太少！'
	elif len(sys.argv) == 3 :
		if not os.path.isdir(sys.argv[1]):
			print u'错误的参数，需要输入一个目录，或者是多个待合并的文件！'

		file_out = open(sys.argv[-1] , 'w')

		in_dir_name = sys.argv[1]
		if not in_dir_name.endswith('/'):
			in_dir_name += '/'
		filenames = os.listdir(in_dir_name )
		happened_set = set()
		first_file = True
		for file_name in filenames:
			if not first_file:
				file_out.write('\n')

			if first_file:
				first_file = False

			f = open(in_dir_name  + file_name ,'r')
			for line in f:
				contents = line.strip().split('\t')
				if len(contents) > 0 and contents[0] in happened_set:
					continue
				happened_set.add(contents[0])
				file_out.write(line)

			f.close()
			
		file_out.close()

	else:
		file_out = open(sys.argv[-1] , 'w')
		happened_set = set()
		first_file = True
		for filename in sys.argv[1:-1]:

			if not first_file:
				file_out.write('\n')

			first_file = False
			
			f = open(filename,'r')
			for line in f:
				contents = line.strip().split('\t')
				if len(contents) > 0 and contents[0] in happened_set:
					continue
				happened_set.add(contents[0])
				file_out.write(line)

			f.close()

		file_out.close()