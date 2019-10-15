import sys,os

dict = {}
wordLen = []

if(len(sys.argv) != 3):
	print ("Invalid Arguments")
	print(sys.argv)
	sys.exit()

if(not(os.path.exists(sys.argv[1]))):
	print ("Invalid File Path")
	sys.exit()

if(sys.argv[2].split('.')[-1] != "txt"):
	print ("Invalid File Format. Only TXT files allowed")
	sys.exit()

with open(sys.argv[2]) as file:
	for line in file:
		for word in line.split():
			dict[word] = dict.get(word,0) + 1

for i in dict:
    print (i,"->",dict[i])