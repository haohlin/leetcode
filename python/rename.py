import os
path = '/Users/linhaohan/Dev/leetcode/python/tree'
for filename in os.listdir(path):
    #print(filename)
    os.rename(os.path.join(path,filename),os.path.join(path, filename.replace(' ', '_').lower())) 