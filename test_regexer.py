from regexer import Regexer as r
from regexer import RegexerString as s

def test_match():
    assert s("Test01 string sentence02")[r"(?P<num>\d+)", 'num'] == ['01', '02']

def test_match_index():
    assert s("Test01 string sentence02")[r"(?P<num>\d+)", 1, 'num'] == '02'

def test_split():
    result = s("Test01 string sentence02") / r"\w\d{2}"
    assert ["Tes", " string sentenc"] == result

def test_remove():
    result = s("Test01 string sentence02") - r"\d"
    assert "Test string sentence" == result
    
def test_regexer():
    num_regex = r(r"(?P<num>\d+)")
    one = num_regex("Test01 string sentence02")
    assert one == [{'num': '01'}, {'num': '02'}]
    assert one["num"] == ['01', '02']
    assert one[0] == {"num": '01'}
    assert num_regex("Test01 string sentence03")["num"] == ['01', '03']