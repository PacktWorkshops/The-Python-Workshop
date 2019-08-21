import import_ipynb
import Exercise13

expected_output = """\
Heavy operation for 1
"""

def test_cached(capsys):
    assert 10 == Exercise13.func(1)
    assert 10 == Exercise13.cached_func(1)
    assert 10 == Exercise13.cached_func(1)
    out, err = capsys.readouterr()
    assert expected_output in out


