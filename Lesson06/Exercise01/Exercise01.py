Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import dataclasses
>>> @dataclasses.dataclass
... class Point:
...   x: int
...   y: int
...
>>> p = Point(x=10, y=20)
>>> print(p)
Point(x=10, y=20)
>>> p2 = Point(x=10, y=20)
>>> p == p2
True
>>> dataclasses.asdict(p)
{'x': 10, 'y': 20}
>>>