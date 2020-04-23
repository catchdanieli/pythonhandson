import os, shutil
import os.path
from os import path

sourcePath = '/home/abbin-pop/Videos/[FreeCourseSite.com] Udemy - Angular 8 - The Complete Guide (2019+ Edition)'
targetPath = '/home/abbin-pop/Videos/SingleSource'

if(path.exists (targetPath)):
    print("Path exists. Removing its contents")
    shutil.rmtree(targetPath)
    os.mkdir(targetPath)

else:
    print("Path does not exist. Creating it.. ")
    os.mkdir(targetPath)

files = []
totalFileCount = 0
currentFileCount = 0

for root, dirs, files in os.walk(sourcePath):
    for file in files:
        if file.endswith(".mp4"):
             totalFileCount = totalFileCount+1
print(totalFileCount)

# r=root, d=directories, f = files
for r, d, f in os.walk(sourcePath):
    for folder in d:
        
        folderNumber = 0
        folderNameSplitted = folder.split(".")
        if len(folderNameSplitted) > 0:
            folderNumber = folderNameSplitted[0] if len(folderNameSplitted[0])>1 else "0"+folderNameSplitted[0]
        for root, directory, files in os.walk(sourcePath + "/" + folder):            
            for file in files:
                if '.mp4' in file:
                    fileNameSplitted = file.split(".")
                    fileNumber = 0
                    if len(fileNameSplitted) > 0:
                        fileNumber = fileNameSplitted[0] if len(fileNameSplitted[0]) > 1 else "0" + fileNameSplitted[0]
                        
                    
                    sourceFile = sourcePath + "/" + folder + "/" + file
                    targetFile = targetPath + "/" + file
                    targetFileRemame = targetPath + "/" + folderNumber + "." + fileNumber + "." + fileNameSplitted[1] + "." + fileNameSplitted[2]
                    currentFileCount = currentFileCount + 1
                    print("Copying " + str(currentFileCount) + " of " + str(totalFileCount) + "..." + targetFileRemame)
                    shutil.copy(sourceFile, targetPath)
                    os.rename(targetFile, targetFileRemame)
        
   
