import sys,os
files = os.listdir('./trainingmodels_data2')
print files
for i in files:
	os.system('java -jar maltparser-1.8.1.jar -c '+i+' -i ./trainingmodels_data2/'+i+' -m learn')
