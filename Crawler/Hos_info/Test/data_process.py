# coding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
	in_file = open(sys.argv[1],'r')
	out_file = open(sys.argv[2],'w')

	data_dict = {}
	for line in in_file:
		if line.startswith('链接到'):
			continue
		if line.startswith('对于'):
			continue
		if line.startswith(' '):
			continue
		if line.startswith('\t'):
			continue
		if line.startswith('用户'):
			continue
		if line.strip() == '':
			continue

		#print line.split('\t')[3].decode('utf-8')
		#raw_input('===================')
		kind = ''
		try:
			kind = line.split('\t')[3]
		except:
			continue

		if data_dict.has_key(kind):
			data_dict[kind].append(line)
		else:
			data_dict[kind] = []
			data_dict[kind].append(line)

	last_line = ''	
	for line in data_dict['三级甲等']:
		if line == last_line:
			continue
		last_line = line
		out_file.write(line)
	for line in data_dict['三级乙等']:
		if line == last_line:
			continue
		last_line = line
		out_file.write(line)
	for line in data_dict['三级丙等']:
		if line == last_line:
			continue
		last_line = line
		out_file.write(line)
	for line in data_dict['二级甲等']:
		if line == last_line:
			continue
		last_line = line
		out_file.write(line)
	for line in data_dict['二级乙等']:
		if line == last_line:
			continue
		last_line = line
		out_file.write(line)
	for line in data_dict['二级丙等']:
		if line == last_line:
			continue
		last_line = line
		out_file.write(line)
	for line in data_dict['一级甲等']:
		if line == last_line:
			continue
		last_line = line
		out_file.write(line)
	for line in data_dict['一级乙等']:
		if line == last_line:
			continue
		last_line = line
		out_file.write(line)
	for line in data_dict['一级丙等']:
		if line == last_line:
			continue
		last_line = line
		out_file.write(line)
	for line in data_dict['未知']:
		if line == last_line:
			continue
		last_line = line
		out_file.write(line)
	in_file.close()
	out_file.close()