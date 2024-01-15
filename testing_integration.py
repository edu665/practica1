import pytest
from text_processing import *


@pytest.mark.parametrize("text, expected",
                        [("Running ran easily and happily","run run easili and happili")])

def test_remove_stemming_lemmatization(text, expected):
    text_remove=perform_stemming(text)
    text_remove=perform_lemmatization(text_remove)
    assert text_remove==expected




@pytest.mark.parametrize("text, expected",
                        [("@pepe le gusta comer pavo el 31"," le gusta comer pavo el "),
                        ("22334455@pepe","")])

def test_remove_number_users(text, expected):
    text_remove=remove_numbers(text)
    text_remove=remove_users(text_remove)
    assert text_remove==expected