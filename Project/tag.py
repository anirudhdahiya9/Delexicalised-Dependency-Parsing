'''
Usage : 
	tag.py file

This script expects an input file with data in CoNNL format as the first argument.
It first extracts all the POS tags in the data and then generates file for each POS tag
where tokens for each POS tag are replaced by '_'
The generated files are named in the format : file_POSTAG
Above, POSTAG is the postag whose tokens are replaced with '_'
'''

from sys import argv
def RepresentsInt(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False

def readtags(fil):
	'''Reads POS Tags of the input file'''	
	f=open(fil,'r')
	data=f.readlines()
	print len(data)
	print 'readlines'
	tag=[]
	for i in range(len(data)):
		data[i]=data[i].split('\t')
		if (len(data[i])>4) and (data[i][4] not in tag):
			tag+=[data[i][4]]
	f.close()
	return tag

fil = argv[1]
tag = readtags(fil)

for r in range(len(tag)):
	tg=tag[r]
	f=open(fil,'r')
	data=f.readlines()
	if tg!='PSP':
		for i in range(len(data)):
			data[i]=data[i].split('\t')
			if((len(data[i])>4) and (data[i][4]==tg)):
				data[i][1]='_'
				data[i][2]='_'
		for i in range(len(data)):
			data[i]='\t'.join(data[i])
		f=open(fil+'_'+tg,'w')
		f.writelines(data)
		f.close()
	else:
		print 'hi'
		for i in range(len(data)):
			data[i]=data[i].split('\t')
			if((len(data[i])>4) and (data[i][4]==tg)):
				data[i][1]='_'
				data[i][2]='_'
		for i in range(len(data)):
			if(len(data[i])>4 and data[i][4] == 'PSP'):
				if RepresentsInt(data[i][6]):
					head = int(data[i][6])
					if head<int(data[i][0]):
						print 'up'
						j = i-int(data[i][0])+head
						if int(head)==int(data[j][0]):
							data[j][5] = data[j][5].split('|')
							data[j][5][5]='vib-'
							data[j][5] = ('|').join(data[j][5])
						#	print data[j][5]
					else:
						print 'down'
						j = i + head - int(data[i][6]) + 1
						if int(head)==int(data[j][0]):
							data[j][5] = data[j][5].split('|')
							data[j][5][5]='vib-'
							data[j][5] = ('|').join(data[j][5])
						#	print data[j][5]				
		for i in range(len(data)):
			data[i]='\t'.join(data[i])
		f=open(fil+'_'+tg,'w')
		f.writelines(data)
		f.close()
