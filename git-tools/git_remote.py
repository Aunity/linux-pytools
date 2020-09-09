#!/usr/bin/env python
'''
@Author ymh
@Email  maohuay@hotmail.com
@Date   2019-10-30 22:44:11
@Web    https://github.com/Aunity
'''
import os
import sys
def main():
    if len(sys.argv[1:])!=2:
        print("Usage: python %s <username> <reponame>"%sys.argv[0])
        sys.exit(0)
    username, reponame = sys.argv[1],sys.argv[2]
    cmd = "git remote add origin https://github.com/%s/%s.git"%(username,reponame)
    #cmd = "git remote add origin git://github.com/%s/%s.git"%(username,reponame)
    print(cmd)
    os.system(cmd)

if __name__ == '__main__':
    main()
