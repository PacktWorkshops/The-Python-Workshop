import import_ipynb
import Exercise12

expected_output = """\
HR audit:
- Area created
- Hired Sam
- Hired Tom

Finance audit:
- Area created
- Used 1000£
"""

def test_report_1(capsys):
    Exercise12.report_audit()
    out, err = capsys.readouterr()
    assert expected_output in out


