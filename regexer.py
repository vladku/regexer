import re

class Regexer:
  """Simplify working with regex.

  Examples:
      ::
          >>> Regexer("Test01 string sentence02")[r"(?P<num>\d+)", 'num']
          ['01', '02']
          >>> Regexer("Test01 string sentence02")[r"(?P<num>\d+)", 1, 'num']
          '02'
          >>> Regexer("Test01 string sentence02") / r"\w\d{2}"
          ['Tes', ' string sentenc']
          >>> Regexer("Test01 string sentence02") - r"\d"
          'Test string sentence'
  
  Raises:
      Exception: type not supported.
      Exception: no item found by index.
  """
  def __init__(self, s):
      self.s = s

  def __sub__(self, other):
      if isinstance(other, str):
          return re.sub(other, "", self.s) 
      else:
          raise Exception(f"Not supported!")  

  def __truediv__(self, other):
      if isinstance(other, str):
          return list(filter(lambda item: item, re.split(other, self.s)))
      else:
          raise Exception(f"Not supported!")

  def __getitem__(self, index):
      if isinstance(index, str):
          return [x.groupdict() for x in re.finditer(index, self.s)]
      r = [x.groupdict() for x in re.finditer(index[0], self.s)]
      if len(index) == 3:
          if len(r) <= index[1]:
              raise Exception(f"There is no item on index {index[1]}")
          return r[index[1]][index[2]]
      elif len(index) == 2 and len(r) == 1:
          return r[0][index[1]]
      else:
        return [x[index[1]] for x in r]