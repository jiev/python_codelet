#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


if __name__ == '__main__':
	file_in = open(sys.argv[1],'r')
	file_out = open(sys.argv[2],'w')

	for line in file_in:
		contents = line.split('\t')
		if len(contents) != 4 :
			continue

		file_out.write(contents[0] + '\t' +contents[1] + '\t' + 'A搜狗' + '\t' +contents[3] )
		file_out.write(contents[0] + '\t' +contents[1] + '\t' + 'B百度' + '\t' +contents[3] )
		file_out.write(contents[0] + '\t' +contents[1] + '\t' + 'C腾讯' + '\t' +contents[3] )
		file_out.write(contents[0] + '\t' +contents[1] + '\t' + 'D高德' + '\t' +contents[3] )

	file_in.close()
	file_out.close()