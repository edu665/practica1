import pytest
from text_processing import *

def test_remove_stopwords():
    text='Me gusta ir al futbol'
    with pytest.raises(ValueError):
        remove_stopwords2(text)


if __name__ == "__main__":
    pytest.main()



    