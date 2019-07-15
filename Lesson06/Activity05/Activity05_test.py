import import_ipynb

def test_report_1(capfd):
    import Activity05
    out, err = capfd.readouterr()
    assert "INFO" in out
    assert "ERROR" in err


