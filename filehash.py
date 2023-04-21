f = open("clone.txt",'r')
data = f.read()
 
data = data.replace("1234","####")

f = open("clone.txt",'w')

f.write(data)

f.close()