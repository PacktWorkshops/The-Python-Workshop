import import_ipynb
import Activity03

def test_report_1(capfd):
    hero = Activity03.Hero()
    assert hero.name == "Superman"
    hero.rename("Batman")
    assert hero.name == "Batman"
    hero.reset_name()
    assert hero.name == "Superman"


