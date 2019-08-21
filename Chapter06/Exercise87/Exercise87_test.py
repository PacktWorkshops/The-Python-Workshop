import import_ipynb
import Exercise03

def test_d1():
    assert str(Exercise03.d1) == "1989-04-24 11:00:00+02:00"


def test_d2():
    assert str(Exercise03.d2) == "1989-04-24 08:00:00-07:00"


def test_d2_madrid():
    assert str(Exercise03.d2_madrid) == "1989-04-24 17:00:00+02:00"
