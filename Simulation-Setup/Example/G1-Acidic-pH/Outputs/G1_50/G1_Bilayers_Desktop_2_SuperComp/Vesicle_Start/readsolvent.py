import sys
import subprocess

# Python implementation to
# read last N lines of a file
 
# Function to read
# last N lines of the file
def LastNlines(fname, N):
    # opening file using with() method
    # so that file get closed
    # after completing work
    with open(fname) as file:
         
        file1 = open("solventstore.txt","w")
        # loop to read iterate
        # last n lines and print it
        for line in (file.readlines() [-N:]):
            print(line, end ='')
            file1.write(line)
            
        file1.close()
 

def read(fname, N):

    with open(fname) as file:
        for line in (file.readlines() [:N]):
            rename = line.split()[1].strip()
        
    
    return rename  
  
            
       

# Driver Code:
if __name__ == '__main__':
    fname = sys.argv[1]
    f1name = "solventstore.txt"
    
    try:
        LastNlines(fname, 2)
        
    except:
        print('File not found')
        
        
    previous = read(f1name, 1)
    now = read(f1name, 2)
    
    print(previous, now)
    
    # If your shell script has shebang, 
    # you can omit shell=True argument.
    print(subprocess.run(["./VesicleY1.bash",previous,now]))
