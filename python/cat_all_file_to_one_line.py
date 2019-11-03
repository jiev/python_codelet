#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import shutil
import os


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print u'输入的文件数量太少！'
	elif len(sys.argv) == 3 :
		if not os.path.isdir(sys.argv[1]):
			print u'错误的参数，需要输入一个目录，或者是多个待合并的文件！'
			sys.exit()

		file_out = open(sys.argv[-1] , 'w')

		in_dir_name = sys.argv[1]
		if not in_dir_name.endswith('/'):
			in_dir_name += '/'
		filenames = os.listdir(in_dir_name )

		first_file = True
		for file_name in filenames:
			if not first_file:
				file_out.write('\n')
			first_file = False

			f = open(in_dir_name  + file_name ,'r')
			for line in f:
				file_out.write(line)

			f.close()
			
		file_out.close()

	else:
		file_out = open(sys.argv[-1] , 'w')

		first_file = True
		for filename in sys.argv[1:-1]:

			if not first_file:
				file_out.write('\n')

			first_file = False
			
			f = open(filename,'r')
			for line in f:
				file_out.write(line)

			f.close()

		file_out.close()