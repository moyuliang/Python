# -*- coding: utf-8 -*-
print 'isn\'t that grand'

big="This is a long string\
that spans two lines."

print big

big="This is a long string \n\
that prints on two lines."

print big

bigger="""
This is an even
bigger string that
spans three lines.
"""

print bigger

big=r"This is a long string\
with a backslash and a new line in it"

print big

mystr="my string"
mystr[0]    #'m'
mystr[-2]   #'n'

mystr[1:4]  #'y s'
mystr[3:]   #'string'
mystr[-3:]  #'ing'

mystr[:3:-1]    #'gnirt' 相当于将3（不包含3）以后的字符逆转

mystr[:3:-2]    #'git  相当于将3以后（不包含3）的字符倒序每隔两个取一个字符

print mystr[2::-1]  #相当于将2（包含2）以前的字符逆转

mystr[1::2] #'ysrn'

print mystr[1::2]


