import import_ipynb
import Exercise11

def test_word_counter_1():
    assert Exercise11.word_counter["DIGIT"] == 10

def test_word_counter_2():
    assert Exercise11.word_counter["QUESTION"] == 2
