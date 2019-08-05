import import_ipynb

def test_report_1(capfd):
    import Activity02
    out, err = capfd.readouterr()
    assert "-11" in out


