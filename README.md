# regexer
Simplify working with regex.

Examples:
```python
>>> Regexer("Test01 string sentence02")[r"(?P<num>\d+)", 'num']
['01', '02']
>>> Regexer("Test01 string sentence02")[r"(?P<num>\d+)", 1, 'num']
'02'
>>> Regexer("Test01 string sentence02") / r"\w\d{2}"
['Tes', ' string sentenc']
>>> Regexer("Test01 string sentence02") - r"\d"
'Test string sentence'
```