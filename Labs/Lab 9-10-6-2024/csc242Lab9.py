'''
Lab 9: File System
10/6/2024
Anthony Zoko
Collaborators: Owen'''
import os
def fileStartsWithCount(folder,chars):
   '''recursive func that searches files with a starting letter
   Uses a for loop to iterate through folders and files'''
   i = 0
   for item in os.listdir(folder):
      n = os.path.join(folder,item)
      if os.path.isdir(n):
         i += fileStartsWithCount(n,chars)

      else:
         if item.startswith(chars):
            i += 1 
   return i
#fileStartsWithCount('/Users/william/Documents/ComputerScience/CSC242-2/Labs/Lab 9-10-6-2024/Test','f')

def countDir(path, dname):
   '''recursive func that searches for a folder name matching dname'''
   i = 0
   for item in os.listdir(path):
      n = os.path.join(path,item)
      if os.path.isdir(n):
         if item.lower() == dname.lower():
            i += 1
         i += countDir(n,dname)
      else:
         pass
      
   return i

#fileStartsWithCount('/Users/william/Documents/ComputerScience/CSC242-2/Labs/Lab 9-10-6-2024/Test','b')