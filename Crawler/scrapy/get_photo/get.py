import urllib

if __name__ == '__main__':
	urls = open('ulrs.txt','r')
	for line in urls.readlines():
		urllib.urlretrieve(line,'./photos/'+(line.strip()).split('/')[-1])
