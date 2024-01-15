import pytest
from text_processing import *


@pytest.mark.parametrize("text, expected",
                        [("running","run"),
                         ("ran","ran")])

def test_perform_stemming(text, expected):
    assert perform_stemming(text)==expected


@pytest.mark.parametrize("text, expected",
                        [("ran","run"),
                         ("easily","easily")])

def test_perform_lemmatization(text, expected):
    assert perform_lemmatization(text)==expected

    

@pytest.mark.parametrize("text, expected",
                        [("1234566ab","ab"),
                         ("1234566 hola como estas"," hola como estas")])

def test_remove_number(text, expected):
    assert remove_numbers(text)==expected


@pytest.mark.parametrize("text, expected",
                        [("@pepito ab"," ab"),
                         ("@verison hola como estas"," hola como estas")])

def test_remove_users(text, expected):
    assert remove_users(text)==expected



if __name__ == "__main__":
    pytest.main()

