import import_ipynb
import Activity01

def test_end_later_than_start(capfd):
    assert Activity01.start < Activity01.end


