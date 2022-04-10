import unittest
from pylox.lexer.tokenizer import Tokenizer
from pylox.lexer.token import Token
from pylox.lexer.token_types import Token_Type

from typing import List

class TestTokenizer(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
      cls.tokenizer = Tokenizer()

   def _create_EOF_token(self):
      return Token(Token_Type.EOF, '', -1, None)

   def test_empty_program(self):
      empty_token = [self._create_EOF_token()]
      tokens, err = self.tokenizer.tokenize("")
      self.assertIsNone(err)
      self.assertEqual(tokens, empty_token)

   def test_whitespace(self):
      lox_program = ' '
      expected_tokens = [self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def _at_end(self):
      lox_program = ''
      self.tokenizer._add_source(lox_program)
      self.assertTrue(self.tokenizer._at_end())

   def test_bang(self):
      lox_program = '!'
      expected_tokens = [Token(Token_Type.BANG, '!', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

      lox_program = '!='
      expected_tokens = [Token(Token_Type.NOT_EQUAL, '!=', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)
   
   def test_comment(self):
      lox_program = '//comment\n !'
      expected_tokens = [Token(Token_Type.BANG, '!', 2, None),self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_equals(self):
      lox_program = '=='
      expected_tokens = [Token(Token_Type.EQUAL_EQUAL, '==', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

      lox_program = '='
      expected_tokens = [Token(Token_Type.EQUAL, '=', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)
   
   def test_greater_equals(self):
      lox_program = '>'
      expected_tokens = [Token(Token_Type.GREATER, '>', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

      lox_program = '>='
      expected_tokens = [Token(Token_Type.GREATER_EQUAL, '>=', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_less_equals(self):
      lox_program = '<='
      expected_tokens = [Token(Token_Type.LESS_EQUAL, '<=', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_tokenizer_single_char(self):
      lox_program = '+'
      expected_tokens = [Token(Token_Type.PLUS, '+', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_tokenizer_small_prog(self):
      lox_program = '-+{}'
      expected_tokens = [
                         Token(Token_Type.MINUS, '-', 1, None),
                         Token(Token_Type.PLUS, '+', 1, None),
                         Token(Token_Type.LEFT_BRACE, '{', 1, None), 
                         Token(Token_Type.RIGHT_BRACE, '}', 1, None),  
                         self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_tokenizer_number(self):
      lox_program = '1.2345'
      expected_tokens = [Token(Token_Type.NUMBER, '1.2345', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_tokenizer_string(self):
      lox_program = '\"hello\"'
      expected_tokens = [Token(Token_Type.STRING, 'hello', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_and_keyword(self):
      lox_program = 'and'
      expected_tokens = [Token(Token_Type.AND, 'and', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_class_keyword(self):
      lox_program = 'class'
      expected_tokens = [Token(Token_Type.CLASS, 'class', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_else_keyword(self):
      lox_program = 'else'
      expected_tokens = [Token(Token_Type.ELSE, 'else', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_false_keyword(self):
      lox_program = 'false'
      expected_tokens = [Token(Token_Type.FALSE, 'false', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_for_keyword(self):
      lox_program = 'for'
      expected_tokens = [Token(Token_Type.FOR, 'for', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_fun_keyword(self):
      lox_program = 'fun'
      expected_tokens = [Token(Token_Type.FUN, 'fun', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_if_keyword(self):
      lox_program = 'if'
      expected_tokens = [Token(Token_Type.IF, 'if', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_nil_keyword(self):
      lox_program = 'nil'
      expected_tokens = [Token(Token_Type.NIL, 'nil', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_or_keyword(self):
      lox_program = 'or'
      expected_tokens = [Token(Token_Type.OR, 'or', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_print_keyword(self):
      lox_program = 'print'
      expected_tokens = [Token(Token_Type.PRINT, 'print', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_return_keyword(self):
      lox_program = 'return'
      expected_tokens = [Token(Token_Type.RETURN, 'return', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_super_keyword(self):
      lox_program = 'super'
      expected_tokens = [Token(Token_Type.SUPER, 'super', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_this_keyword(self):
      lox_program = 'this'
      expected_tokens = [Token(Token_Type.THIS, 'this', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_true_keyword(self):
      lox_program = 'true'
      expected_tokens = [Token(Token_Type.TRUE, 'true', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_var_keyword(self):
      lox_program = 'var'
      expected_tokens = [Token(Token_Type.VAR, 'var', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_while_keyword(self):
      lox_program = 'while'
      expected_tokens = [Token(Token_Type.WHILE, 'while', 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

   def test_identifiers(self):
      lox_program = 'identifier'
      expected_tokens = [Token(Token_Type.IDENTIFIER, lox_program, 1, None), self._create_EOF_token()]
      returned_tokens, err = self.tokenizer.tokenize(lox_program)
      self.assertIsNone(err)
      self.assertEqual(returned_tokens, expected_tokens)

if __name__ == '__main__':
   unittest.main()