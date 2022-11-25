lookup = 'DPPC'
numbers=[]


with open('combined.gro','r') as myFile:
    for num, line in enumerate(myFile, 1):
        if lookup in line:
            ##print('found at line:%i' %(num))
            txt=str(line)
            x=txt.split()
            ##print(x[0])
            for word in x[0]:
                if word.isdigit():
                    numbers.append(int(word))
                    

            print(int(''.join([str(item) for item in numbers]))-1)
                
            break
            

