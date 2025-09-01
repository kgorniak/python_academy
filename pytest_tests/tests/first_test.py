def dodaj_jeden(x):
    return x + 1


def test_pass():
    """
    Test sprawdza czy dodanie jeden do cztery daje piÄ™Ä‡.
    """
    assert dodaj_jeden(4) == 5


def test_failure():
    """
    Test sprawdza czy dodanie jeden do cztery daje szeÅ›Ä‡.
    """
    assert dodaj_jeden(4) == 6