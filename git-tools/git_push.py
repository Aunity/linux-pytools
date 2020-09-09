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
    if len(sys.argv)==1:
        args = ""
    else:
        args = " ".join(sys.argv[1:])
    if not len(args):
        cmd = "git push -u origin master"
    else:
        cmd = "git push %s"%args
    print(cmd)
    os.system(cmd)

if __name__ == '__main__':
    main()
