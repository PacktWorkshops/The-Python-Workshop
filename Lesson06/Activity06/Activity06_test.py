import import_ipynb
import Activity06

def test_report_1(capfd):
    hero = Activity06.Hero()
    assert hero.name == "Superman"
    hero.rename("Batman")
    assert hero.name == "Batman"
    hero.reset_name()
    assert hero.name == "Superman"


