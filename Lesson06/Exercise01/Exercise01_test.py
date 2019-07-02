import import_ipynb
import dataclasses
import Exercise01

def test_class_creation():
    c = Exercise01.Point(x=1, y=2)
    c.x == 1
    c.y == 3

def test_class_as_dict():
    c = Exercise01.Point(x=1, y=2)
    assert {'x': 1, 'y': 2} == dataclasses.asdict(c)

def test_class_as_str():
    c = Exercise01.Point(x=1, y=2)
    assert "Point(x=1, y=2)" == str(c)
