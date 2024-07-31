'''


take the input of the master password.
take the input whether user wants to add new passwd or view existing ones and q for quit in lower input.
if mode is quit break
if mode is view => call the view function
elif mode is add => call the add function
else invalid
write functions for view and add .
Add function: 
    take name as input name
    take password as input password.
    Create a file if doesnt exist , if exist open the file
    with open('password.txt','a/w/d') as f: /// the "with" will automatically close
    if you exclude it u must close the file.
    f.write("name"+"|"+"pwd"+"\n")
    
view function:
    with open("filename","r") aas f:
    for line in r.readlines():
        data = print(line.rstrip()) //removes the whitespaces
        user,passw=data.split("|") gives the output in list format
        print("user",user,,"password",password)
        

'''
def write():
    with open("file_name.txt","a")as f:
        name=input("enter name: ")
        passwd=input("enter password: ")
              
        f.write(name+"|"+passwd+"\n")
        
def read():
    with open("file_name.txt","r") as r:
        for line in r.readlines():
            data=line.rstrip()
            user,passwd=data.split("|")
            print("user ",user,"passwd ",passwd)


master=input("enter the master password")
while True:
    input_type=input("read,write,quit")
    if input_type=="quit":
        break
    elif input_type=="read":
        read()
    elif input_type=="write":
        write()
    else:
        print("invalid input")
        break
