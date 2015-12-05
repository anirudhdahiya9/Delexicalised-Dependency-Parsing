import sys,os
trfiles = os.listdir('./training_data/')
print str(trfiles)
for i in trfiles:
	os.system('java -jar maltparser-1.8.1.jar -c '+i+' -i ./training_data/'+i+' -m learn')
	
