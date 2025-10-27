import os  
import sys

def keep():
    files_counter = 0
    files_counter1 = 0
    folder_counter =0
    files_counter2 =0
    si="\\"
        
    print("\nThis program keeps all files with your keyword")
    loc = str(input("Enter the location:\n"))
    keyword= str(input("Enter the keyword:\n"))
    for (root,dirs,files) in os.walk(loc, topdown=True):
        for file in files:
            if file.find(keyword)!=-1:
                files_counter+=1
            else:
                files_counter2 +=1
                os.remove(root+si+file)
        files_counter1+= len(files)
        folder_counter+= len(dirs)

    print("\n**RECAP**")   
    print('Number of files found: {}'.format(files_counter1))
    print('Number of files starting with {} and kept: {}'.format(keyword,files_counter))
    print('Number of files deleted: {}'.format(files_counter2))
    print('Number of folders found: {}'.format(folder_counter))

    input("\nEnter any key to quit.") 
    sys.exit() 

def delete():
    files_counter = 0
    files_counter1 = 0
    folder_counter =0
    files_counter2 =0
    si="\\"
        
    print("\nThis program deletes all files with your keyword")
    loc = str(input("Enter the location:\n"))
    keyword= str(input("Enter the keyword:\n"))
    for (root,dirs,files) in os.walk(loc, topdown=True):
        for file in files:
            if file.find(keyword)!=-1:
                files_counter+=1
                os.remove(root+si+file)
            else:
                files_counter2 +=1
        files_counter1+= len(files)
        folder_counter+= len(dirs)

    print("\n**RECAP**")     
    print('Number of files found: {}'.format(files_counter1))
    print('Number of files starting with {} and deleted: {}'.format(keyword,files_counter))
    print('Number of files kept: {}'.format(files_counter2))
    print('Number of folders found: {}'.format(folder_counter))

    input("\nEnter any key to quit.") 
    sys.exit() 

def keyswitch():
    print("\nThis program changes the keyword in all files")
    path_folder = str(input("Enter the location:\n"))
    keyword = str(input("Enter the old keyword:\n"))
    keyword1 =str(input("Enter the new keyword:\n"))

    files_counter = 0
    total=0

    for (root,dirs,files) in os.walk(path_folder, topdown=True):
        print("\nPath = ",root)
        for file in files:
            total+=1
            if file.find(keyword)!=-1:
                files_counter +=1
                file1=file.replace(keyword,keyword1)
                os.rename(root+"\\"+file,root+"\\"+file1)
                print(file,"-->",file1)

    print()        
    print('** RECAP **')
    print('Number of files found: {}'.format(total))
    print('Number of files edited: {}'.format(files_counter))
    
    input("\nEnter any key to quit.") 
    sys.exit() 

def ext_edit():
    print("\nThis program changes the extension of files with keyword")
    path_folder = str(input("Enter the location:\n"))
    keyword = str(input("Enter the keyword:\n"))
    new_ext = str(input("Enter the new extension of file:\n"))

    files_counter = 0
    total=0

    for (root,dirs,files) in os.walk(path_folder, topdown=True):
        print("\nPath = ",root)
        for file in files:
            total+=1
            filename,ext = os.path.splitext(file)
            if file.find(keyword)!=-1:
                files_counter +=1
                soo=file.replace(ext,new_ext) 
                os.rename(root+"\\"+file,root+"\\"+soo) 
                print(file,"-->",soo)

    print()        
    print('** RECAP **')
    print('Number of files found: {}'.format(total))
    print('Number of files edited: {}'.format(files_counter))
    
    input("\nEnter any key to quit.") 
    sys.exit() 

def both_up():
    print("\nThis program makes both the name and extension of all files uppercase")
    path_folder = str(input("Enter the location:\n"))

    files_counter = 0

    for (root,dirs,files) in os.walk(path_folder, topdown=True):
        print("\nPath = ",root)
        for file in files:
            filename,ext = os.path.splitext(file)
            new_path= filename.upper() + ext.upper()
            os.rename(root+"\\"+file,root+"\\"+new_path)
            files_counter +=1
            print(file,"-->",new_path)
    
    print()        
    print('** RECAP **')
    print('Number of files edited: {}'.format(files_counter))

    input("\nEnter any key to quit.") 
    sys.exit() 

def name_up():
    print("\nThis program makes only the name of files uppercase")
    path_folder = str(input("Enter the location:\n"))

    files_counter = 0

    for (root,dirs,files) in os.walk(path_folder, topdown=True):
        print("\nPath = ",root)
        for file in files:
            filename,ext = os.path.splitext(file)
            new_path= filename.upper() + ext
            os.rename(root+"\\"+file,root+"\\"+new_path)
            files_counter +=1
            print(file,"-->",new_path)
    
    print()        
    print('** RECAP **')
    print('Number of files edited: {}'.format(files_counter))

    input("\nEnter any key to quit.") 
    sys.exit() 

def ext_up():
    print("\nThis program makes only the extension of files uppercase")
    path_folder = str(input("Enter the location:\n"))

    files_counter = 0

    for (root,dirs,files) in os.walk(path_folder, topdown=True):
        print("\nPath = ",root)
        for file in files:
            filename,ext = os.path.splitext(file)
            new_path= filename + ext.upper()
            os.rename(root+"\\"+file,root+"\\"+new_path)
            files_counter +=1
            print(file,"-->",new_path)
    
    print()        
    print('** RECAP **')
    print('Number of files edited: {}'.format(files_counter))

    input("\nEnter any key to quit.") 
    sys.exit() 

def both_down():
    print("\nThis program makes both the name and extension of all files lowercase")
    path_folder = str(input("Enter the location:\n"))

    files_counter = 0

    for (root,dirs,files) in os.walk(path_folder, topdown=True):
        print("\nPath = ",root)
        for file in files:
            filename,ext = os.path.splitext(file)
            new_path= filename.lower() + ext.lower()
            os.rename(root+"\\"+file,root+"\\"+new_path)
            files_counter +=1
            print(file,"-->",new_path)
    
    print()        
    print('** RECAP **')
    print('Number of files edited: {}'.format(files_counter))

    input("\nEnter any key to quit.") 
    sys.exit() 

def name_down():
    print("\nThis program makes only the name of files lowercase")
    path_folder = str(input("Enter the location:\n"))

    files_counter = 0

    for (root,dirs,files) in os.walk(path_folder, topdown=True):
        print("\nPath = ",root)
        for file in files:
            filename,ext = os.path.splitext(file)
            new_path= filename.lower() + ext
            os.rename(root+"\\"+file,root+"\\"+new_path)
            files_counter +=1
            print(file,"-->",new_path)
    
    print()        
    print('** RECAP **')
    print('Number of files edited: {}'.format(files_counter))

    input("\nEnter any key to quit.") 
    sys.exit() 

def ext_down():
    print("\nThis program makes only the extension of files lowercase")
    path_folder = str(input("Enter the location:\n"))

    files_counter = 0

    for (root,dirs,files) in os.walk(path_folder, topdown=True):
        print("\nPath = ",root)
        for file in files:
            filename,ext = os.path.splitext(file)
            new_path= filename + ext.lower()
            os.rename(root+"\\"+file,root+"\\"+new_path)
            files_counter +=1
            print(file,"-->",new_path)
    
    print()        
    print('** RECAP **')
    print('Number of files edited: {}'.format(files_counter))

    input("\nEnter any key to quit.") 
    sys.exit() 

def ext_new():
    print("\nThis program changes the extension of files ")
    path_folder = str(input("Enter the location:\n"))
    ext1 = str(input("Enter the old extension of file:\n"))
    ext2 = str(input("Enter the new extension of file:\n"))

    files_counter = 0
    total=0

    for (root,dirs,files) in os.walk(path_folder, topdown=True):
        print("\nPath = ",root)
        for file in files:
            total+=1
            filename,ext = os.path.splitext(file)
            if file.find(ext1)!=-1:
                files_counter +=1
                soo=file.replace(ext,ext2)
                os.rename(root+"\\"+file,root+"\\"+soo) 
                print(file,"-->",soo)

    print()        
    print('** RECAP **')
    print('Number of files found: {}'.format(total))
    print('Number of files edited: {}'.format(files_counter))
    
    input("\nEnter any key to quit.") 
    sys.exit()   
    
def all_files():
    files_counter1 = 0
    files_counter =0
    si="\\"
    
    print("\nThis program changes the location of all files in a specific folder")
    loc = str(input("Enter the current location:\n"))
    new_loc= str(input("Enter the new location:\n"))
    for (root,dirs,files) in os.walk(loc ):
        for file in files:
            s= os.path.basename(root)
            os.mkdir(new_loc+si+s)
            os.replace(root+si+file , new_loc+si+s+si+file)
            files_counter+=1
        files_counter1+= len(files)
    print("\n**RECAP**")   
    print('Number of files found: {}'.format(files_counter1))
    print('Number of files moved: {}'.format(files_counter))
    input("\nEnter any key to quit.") 
    sys.exit() 
    
def keyword_inc():
    files_counter = 0
    files_counter1 = 0
    files_counter2 =0
    si="\\"
    
    print("\nThis program moves all files with specific keywords in a folder")
    loc = str(input("Enter the location:\n"))
    keyword= str(input("Enter the keyword:\n"))
    new_loc= str(input("Enter the new location:\n"))
    for (root,dirs,files) in os.walk(loc, topdown=True):
        for file in files:
            if file.find(keyword)!=-1:
                files_counter+=1
                s= os.path.basename(root)
                os.mkdir(new_loc+si+s)
                os.replace(root+si+file , new_loc+si+s+si+file)
            else:
                files_counter2 +=1
        files_counter1+= len(files)

    print("\n**RECAP**")     
    print('Number of files found: {}'.format(files_counter1))
    print('Number of files starting with {} and relocated: {}'.format(keyword,files_counter))
    print('Number of files kept: {}'.format(files_counter2))

    input("\nEnter any key to quit.") 
    sys.exit() 
    
def ext_inc():
    files_counter = 0
    files_counter1 = 0
    files_counter2 =0
    si="\\"
    
    print("\nThis program moves all files with specific extensions in a folder")
    loc = str(input("Enter the location:\n"))
    ext1 = str(input("Enter the extension format:\n"))
    new_loc= str(input("Enter the new location:\n"))
    for (root,dirs,files) in os.walk(loc, topdown=True):
        for file in files:
            filename,ext = os.path.splitext(file)
            if file.find(ext1)!=-1:
                files_counter+=1
                s= os.path.basename(root)
                os.mkdir(new_loc+si+s)
                os.replace(root+si+file , new_loc+si+s+si+file)
            else:
                files_counter2 +=1
                files_counter1+= len(files)

    print("\n**RECAP**")     
    print('Number of files found: {}'.format(files_counter1))
    print('Number of files with extension {} and relocated: {}'.format(ext1,files_counter))
    print('Number of files kept: {}'.format(files_counter2))

    input("\nEnter any key to quit.") 
    sys.exit() 
     
print("Choose from the options below:")
print("1.Edit Files with Keywords")
print("2.Edit the case of filenames")
print("3.Edit the extension of files")
print("4.Change location of files")
opt = int(input("Enter your option number:"))

if opt==1:
    print("\nFiles with Keywords")
    print("1.Keep all files with a keyword")
    print("2.Delete all files with a keyboard")
    print("3.Edit keyword in files")
    print("4.Edit extension of files with keyword")
    opt = int(input("Enter your option number:"))
    if opt==1:
        keep()
    if opt==2:
        delete()
    if opt==3:
        keyswitch()
    if opt==4:
        ext_edit()
    else:
        print("\nInvalid Input!!!")
        input("Enter any key to quit.") 
        sys.exit() 
if opt==2:
    print("\nCase of Filenames")
    print("1.Make uppercase")
    print("2.Make lowercase")
    opt = int(input("Enter your option number:"))
    if opt==1:
        print("\n1.Make both name and extension of all files uppercase")
        print("2.Make only the name of all files uppercase")
        print("3.Make only the extension of all files uppercase")
        opt = int(input("Enter your option number:"))
        if opt==1:
            both_up()
        if opt==2:
            name_up()
        if opt==3:
            ext_up()
        else:
            print("\nInvalid Input!!!")
            input("Enter any key to quit.") 
            sys.exit() 
    if opt==2:
        print("\n1.Make both name and extension of all files lowercase")
        print("2.Make only the name of all files lowercase")
        print("3.Make only the extension of all files lowercase")
        opt = int(input("Enter your option number:"))
        if opt==1:
            both_down()
        if opt==2:
            name_down()
        if opt==3:
            ext_down()
        else:
            print("\nInvalid Input!!!")
            input("Enter any key to quit.") 
            sys.exit() 
    else:
        print("\nInvalid Input!!!")
        input("Enter any key to quit.") 
        sys.exit() 
    
if opt==3:
    ext_new()
if opt==4:
    print("\nLocation of files")
    print("1.All files in a folder")
    print("2.Files with keyword")
    print("3.Files with specific extensions")
    opt = int(input("Enter your option number:"))
    if opt==1:
        all_files()
    if opt==2:
        keyword_inc()
    if opt==3:
        ext_inc()
    else:
        print("\nInvalid Input!!!")
        input("Enter any key to quit.") 
        sys.exit() 
else:
    print("\nInvalid Input!!!")
    input("Enter any key to quit.") 
    sys.exit() 

