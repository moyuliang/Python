# -*- coding: utf-8 -*-
# @Version: Python3.6.5
# @Time: 8/12/2018 8:52 PM
# @Author  : Jacklyn

# pw.py - An insecure password locker program.
PASSWORDS = {'email': 'WYQshishi95',
             'blog': '1995test',
             'luggage': '123456'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
