#!python3
# panic3.py - Transforming the string "Don't panic!" into the string "on tap" using slice notation
#             w/ one line for the new_phrase statement

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = ''.join(plist[1:3]) + ''.join([plist[5], plist[4], plist[7], plist[6]])

print(plist)
print(new_phrase)