from regexer import RegexerString as r

def test_match():
    assert r("Test01 string sentence02")[r"(?P<num>\d+)", 'num'] == ['01', '02']

def test_match_index():
    assert r("Test01 string sentence02")[r"(?P<num>\d+)", 1, 'num'] == '02'

def test_split():
    result = r("Test01 string sentence02") / r"\w\d{2}"
    assert ["Tes", " string sentenc"] == result

def test_remove():
    result = r("Test01 string sentence02") - r"\d"
    assert "Test string sentence" == result