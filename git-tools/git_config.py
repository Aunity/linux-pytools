#!/usr/bin/env python
'''
@Author ymh
@Email  maohuay@hotmail.com
@Date   2019-10-30 21:42:28
@Web    https://github.com/Aunity
'''
import os
import sys
def main():
    if len(sys.argv[1:]) != 2:
        print('Usage:python %s <username> <email>'%sys.argv[0])
        sys.exit(0)
    username, email = sys.argv[1:]
    cmd0 = '''git config --global user.name "%s"'''%username
    cmd1 = '''git config --global user.email "%s"'''%email
    print(cmd0)
    print(cmd1)
    os.system(cmd0)
    os.system(cmd1)

if __name__ == '__main__':
    main()
