from typing import List
import math

print('Karakterláncok kezelése')
a: str = 'Hello, World!'
print('String, mint karakter lista')
print(a)  # Hello, World!
print(a[1])  # e
print(type(a[1]))  # <class 'str'> mivel nincs karakter típus a Python-ban
print(a[1:5])  # ello
print(a[-6:-3])  # Wor
print(a[7:])  # World!

print('String hossza')
print(len(a))  # 13 (szóközzel, írásjelekkel)

print('String darabolása a split() metódussal')
# Syntax: string.split(separator, maxsplit)
# maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
m: List[str] = a.split()  # alapértelmezetten a szóköznél darabol (vág)
# a szóköz nem kerül bele a létrejövő új listába:
print(m)  # ['Hello,', 'World!']
m: List[str] = a.split('o')
print(m)  # ['Hell', ', W', 'rld!']
m: List[str] = a.split(', ')  # Megadhatunk több karaktert is!
print(m)  # ['Hello', 'World!']

print('Új string összeállítása template string-et használva')
b: str = f'{a[:5]} Python! {math.pi:.2f}'
print(b)

print('Tartalmazásvizsgálat: in és not in operátorok')
print('World' in a)  # True
print('world' not in a)  # True (kis- és nagybetű érzékeny a vizsgálat)


# String bejárása (karakterekként)
for i in a:
    print(i, end=' ')  # H e l l o ,   W o r l d !
print()

# Fontosabb string metódusok
print('\t\ralma \n'.strip())  # alma (whitespace karaktereket levágja a string elején és végén)
print('ÁRVÍZTŰRŐ TÜKÖRFÚRÓGÉP'.lower())  # árvíztűrő tükörfúrógép
print('árvíztűrő tükörfúrógép'.upper())  # ÁRVÍZTŰRŐ TÜKÖRFÚRÓGÉP
print(a.replace("o", "@"))  # Hell@, W@rld! (összes előfordulást cseréli)
print(a.count('l'))  # 3


# String metódusok angol leírása:

# capitalize()	Converts the first character to upper case
# swapcase() Swaps cases, lower case becomes upper case and vice versa
# title() Converts the first character of each word to upper case

# startswith()	Returns true if the string starts with the specified value
# endswith()	Returns true if the string ends with the specified value

# find()	Searches the string for a specified value and returns the first position of where it was found
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# -1 lesz a visszatérési értéke, ha a keresett string nem található

# index()	Searches the string for a specified value and returns the first position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# Hibát dob, ha a keresett string nem található

# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal() Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# islower()	Returns True if all characters in the string are lower case
# isnumeric() Returns True if all characters in the string are numeric
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
# isupper()	Returns True if all characters in the string are upper case

# join() Takes all items in an iterable and joins them into one string. Syntax: separator_string.join(iterable)

# strip() Returns a trimmed version of the string
# lstrip() Returns a left trim version of the string
# rstrip() Returns a right trim version of the string

# split() Splits the string at the specified separator, and returns a list. Syntax: string.split(separator, maxsplit)
# rsplit() Splits the string at the specified separator, and returns a list. Syntax: string.rsplit(separator, maxsplit)
# splitlines() Splits the string at line breaks and returns a list
