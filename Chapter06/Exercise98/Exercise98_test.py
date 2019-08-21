import import_ipynb

def test_report_1(capfd):
    import Exercise14
    Exercise14.print_stderr("Hello")
    out, err = capfd.readouterr()
    assert "Hello" in err


