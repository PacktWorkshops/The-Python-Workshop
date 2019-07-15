Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Inte
l)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> bookstore = 'City Lights'
>>> bookstore = 'City Lights"
  File "<stdin>", line 1
    bookstore = 'City Lights"
                            ^
SyntaxError: EOL while scanning string literal
>>> bookstore = "Moe's"
>>> bookstore = 'Moe's'
  File "<stdin>", line 1
    bookstore = 'Moe's'
                     ^
SyntaxError: invalid syntax
>>>