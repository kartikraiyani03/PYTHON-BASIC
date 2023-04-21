f = open("log.txt",'w')
data = True
i=0     
while(data):
    data = f.readline()
    if "hey" in data.lower():
         print(data)
         print("Key Founded at",i)
    else:
        print("Key not Founded")
    i=i+1   
f.close()

     

