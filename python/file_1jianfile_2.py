#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


if __name__ == '__main__':
	file_1 = open(sys.argv[1],'r')
	file_2 = open(sys.argv[2],'r')
	file_3 = open(sys.argv[3],'w')

	file_1_set = set()
	file_2_set = set()
	for line in file_1:
		if len(line.strip()) > 0:
			file_1_set.add(line.rstrip())

	for line in file_2:
		if len(line.strip()) > 0:
			file_2_set.add(line.rstrip())

	file_3.write('in ' + sys.argv[1] +' but not in ' + sys.argv[2] + '\n')
	for item in file_1_set:
		if item not in file_2_set:
			file_3.write(item + '\n')

	file_3.write('\n\n')
	file_3.write('in ' + sys.argv[2] +' but not in ' + sys.argv[1] + '\n')
	for item in file_2_set:
		if item not in file_1_set:
			file_3.write(item + '\n')


	file_1.close()
	file_2.close()
	file_3.close()