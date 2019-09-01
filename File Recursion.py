import os

def getListOfFiles(dirName,extention):
    ls=[]
     
    # names in the given directory 
    listOfFile = os.listdir(dirName)# create a list of file and sub directories
    allFiles = []#list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        
        if os.path.isdir(fullPath):# If entry is a directory then get the list of files in this directory
            
            allFiles = allFiles + getListOfFiles(fullPath,extention)
        else:
            allFiles.append(fullPath)
    for i in range(len(allFiles)):    
        if (allFiles[i].endswith(extention)):
            ls=ls+[allFiles[i]]
    return ls#allFiles
        

def main():
    #test case 1
    dirName= 'D:\Python'
    extention= ".c"
    ll=[]
    if os.path.isdir(dirName):
        ll=getListOfFiles(dirName,extention)
        if not ll:
            print("there is no file with such extention")
        else:    
            print(ll)
    else:
        printf("enter a valid directory")
    #answer is-
    #['D:\\Python\\subdir1\\a.c', 'D:\\Python\\subdir3\\subsubdir1\\b.c', 'D:\\Python\\subdir5\\a.c', 'D:\\Python\\t1.c', 'D:\\Python\\tcl\\nmake\\nmakehlp.c']    

    
    #test case 2
    dirName= 'D:\Python'
    extention= ".abc"
    ll=[]
    if os.path.isdir(dirName):
        ll=getListOfFiles(dirName,extention)
        if not ll:
            print("there is no file with such extention")
        else:
            print(ll)
    else:
        printf("enter a valid directory")
    #answer
    #there is no file with such extention
    

    #test case 3
    dirName= 'F:\Python'
    extention= ".c"
    ll=[]
    if os.path.isdir(dirName):
        ll = getListOfFiles(dirName,extention)
        if not ll:
            print("there is no file with such extention")
        else:
            print(ll)
    else:
        print("enter a valid directory")
    #answer
    #enter a valid directory
        
    
    return
if __name__ == '__main__':
    main()
