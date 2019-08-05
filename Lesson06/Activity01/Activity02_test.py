import import_ipynb
import Activity02

def test_end_later_than_start(capfd):
    assert Activity02.start < Activity02.end


