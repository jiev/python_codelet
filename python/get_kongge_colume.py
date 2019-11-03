#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


if __name__ == '__main__':
	file_in = open(sys.argv[1],'r')
	file_out = open(sys.argv[2],'w')

	columes = [int(x) for x in sys.argv[3].split(',')]

	for line in file_in:
		contents = line.strip().split(' ')
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