#encoding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
	file_in = open(sys.argv[1],'r')
	file_out = open(sys.argv[2],'w')

	happened_set = set()

	count = 0
	for line in file_in:
		count += 1
		if count % 10000 == 0 :
			print count

		line = line.strip();
		if len(line) == 0 :
			continue

		try:
			contents = line.split('\t')
			for c in contents:
				if c in happened_set:
					continue
				else:
					happened_set.add(c)
					file_out.write(c + '\n')
		except:
			print 'something wrong'
			continue


	file_in.close()
	file_out.close()

