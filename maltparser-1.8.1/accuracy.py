import os
from sys import argv
def accuracy(input_file,output_file):
	f=open(input_file,'r')
	lin = f.readlines()
	f.close()
	f = open(output_file,'r')
	lout = f.readlines()
	f.close()
	for i in range(len(lout)):
		lout[i] = lout[i].split('\t')
		lin[i] = lin[i].split('\t')
	tc = 0
	mc = 0
	for i in range(len(lout)):
		if len(lout[i])>6:
			if lout[i][-3] == lin[i][-3]:
				mc+=1
			tc+=1
	return tc,mc

input_file = argv[1]
path = argv[2]

result_files = os.listdir(path)
for i in result_files:
	outfile = path+'/'+i
	tc,mc = accuracy(input_file,outfile)
	ratio = float(mc)/float(tc)
	print i
	print ratio
	ratio *=100.0
	f=open(input_file+'__report2'+'.txt','a')
	if(len(i.split('_'))>2):
		tg = i.split('_')[2].split('.')[0]
	else:
		tg = 'FULL'
	wr = ['Tag : '+tg,'Total Count : '+str(tc),'Match Count : '+str(mc),'Accuracy : '+str(ratio),'']
	for x in range(len(wr)):
		wr[x] = wr[x] + '\n'
	f.writelines(wr)
	f.close()
