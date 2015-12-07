import os
files = os.listdir('.')

for fil in files:
	if fil.endswith('mco'):
		os.system('java -jar maltparser-1.8.1.jar -c '+fil+' -i testing.dat -o itestingoutput2/out_'+fil+'.conll -m parse')
