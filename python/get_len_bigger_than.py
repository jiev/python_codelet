#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


if __name__ == '__main__':
	file_in = open(sys.argv[1],'r')
	file_out = open(sys.argv[2],'w')

	columes = [int(x) for x in sys.argv[3].split(',')]

	if len(columes) != 2:
		print 'you input the wrong parameter!'
		sys.exit()

	limit_len = int(columes[1])
	colume = int(columes[0])
	for line in file_in:
		contents = line.strip().split('\t')
		if len(contents) < colume + 1:
			continue

		if len(contents[colume].decode('utf-8')) > limit_len:
			file_out.write(line)


	file_in.close()
	file_out.close()


