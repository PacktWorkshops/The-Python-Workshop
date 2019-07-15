import import_ipynb
import Exercise05

def test_epoch():
    assert str(Exercise05.epoch)[:-15] == "1970-01-01 00:00:"
