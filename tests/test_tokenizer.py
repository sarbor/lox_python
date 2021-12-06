import unittest
from pylox.lexer.tokenizer import Tokenizer
from pylox.lexer.token import Token
from pylox.lexer.token_types import Token_Type

from typing import List

class TestTokenizer(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
      cls.tokenizer = Tokenizer()
   
   def _test_tokenize(self, test_string="") -> List[Token]:
      return self.tokenizer.tokenize(test_string)

   def _create_EOF_token(self) -> Token:
      return Token(Token_Type.EOF, '', -1, None)

   def test_empty_program(self):
      empty_token = [self._create_EOF_token()]
      self.assertEqual(self._test_tokenize(""), empty_token)

   def test_tokenizer_single_char(self):
      lox_program = '+'
      expected_tokens = [Token(Token_Type.PLUS, '+', 1, None), self._create_EOF_token()]
      returned_tokens = self.tokenizer.tokenize(lox_program)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_tokenizer_small_prog(self):
      lox_program = '-+{}'
      expected_tokens = [
                         Token(Token_Type.MINUS, '-', 1, None),
                         Token(Token_Type.PLUS, '+', 1, None),
                         Token(Token_Type.LEFT_BRACE, '{', 1, None), 
                         Token(Token_Type.RIGHT_BRACE, '}', 1, None),  
                         self._create_EOF_token()]
      returned_tokens = self.tokenizer.tokenize(lox_program)
      self.assertEqual(returned_tokens, expected_tokens)

if __name__ == '__main__':
   unittest.main()
