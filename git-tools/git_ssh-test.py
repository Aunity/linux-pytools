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
    cmd = "ssh -T git@github.com"
    print(cmd)
    os.system(cmd)

if __name__ == '__main__':
    main()
