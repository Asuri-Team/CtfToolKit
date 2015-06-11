#!/usr/bin/env python
# coding=utf-8

"""
UCS-4 range (hex.) UTF-8 octet sequence (binary)

0000 0000-0000 007F 0xxxxxxx
0000 0080-0000 07FF 110xxxxx 10xxxxxx
0000 0800-0000 FFFF 1110xxxx 10xxxxxx 10xxxxxx
0001 0000-001F FFFF 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
"""

import struct

if __name__ == "__main__":
    for string in ['中文', u'中文']:

        print string, len(string)

        for c in string:
            print bin(ord(c)),

        print