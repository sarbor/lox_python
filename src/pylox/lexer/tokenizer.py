from pylox.lexer.token import Token 
from typing import List, Optional
from pylox.lexer.token_types import Token_Type
from pylox.err import Lox_Err

class Tokenizer:
   def __init__(self):
      self.tokens = []
      self.source = ""
      self.current = 0
      self.start = 0
      self.line_num = 1
      self.error = None

   def _current_text(self) -> str:
      return self.source[self.start:self.current+1]

   def _add_source(self, text: str) -> None:
      self.tokens = []
      self.source = text
      self.current = 0
      self.start = 0
      self.line_num = 1

   def _add_token(self, token_type: Token_Type) -> None:
      if token_type == Token_Type.EOF:
         lexeme = ''
         self.line_num = -1
      else:
         lexeme = self._current_text()

      token = Token(token_type, lexeme, self.line_num, None)
      self.tokens.append(token)

   def tokenize(self, text: str) -> List[Token]:
      err = None
      self._add_source(text)

      while not self._at_end():
         token_type, err = self.scan_token_type()
         if err:
            return None, err
         if token_type:
            self._add_token(token_type)

         self._increment_cursor()
         self.start = self.current

      self._add_token(Token_Type.EOF)

      return self.tokens, err

   def _at_end(self) -> bool:
      return self.current >= len(self.source) 

   def _increment_cursor(self) -> None:
      self.current += 1

   def _decrement_cursor(self) -> None:
      self.current -= 1

   def _peek(self) -> Optional[str]:
      next_text = None
      self._increment_cursor()
      if not self._at_end():
         next_text = self.source[self.current]
      self._decrement_cursor()
      return next_text

   def scan_token_type(self) -> Token_Type:
      current_text = self._current_text()
      err = None
      if current_text == '(':
         return Token_Type.LEFT_PAREN, err
      elif current_text == ')':
         return Token_Type.RIGHT_PAREN, err
      elif current_text == '{':
         return Token_Type.LEFT_BRACE, err
      elif current_text == '}':
         return Token_Type.RIGHT_BRACE, err
      elif current_text == ',':
         return Token_Type.COMMA, err
      elif current_text == '.':
         return Token_Type.DOT, err
      elif current_text == '-':
         return Token_Type.MINUS, err
      elif current_text == '+':
         return Token_Type.PLUS, err
      elif current_text == ';':
         return Token_Type.SEMICOLON, err
      elif current_text == '/':
         if self._peek() == '/':
            while (next_char := self._peek()) != '\n' and next_char:
               self._increment_cursor()

            return None, err
         return Token_Type.SLASH, err
      elif current_text.isdigit():
         return self._get_number_token()
      elif current_text == '*':
         return Token_Type.STAR, err
      elif current_text == '!':
         if self._peek() == '=':
            self._increment_cursor() 
            return Token_Type.NOT_EQUAL, err

         return Token_Type.BANG, err
      elif current_text == '=':
         if self._peek() == '=':
            self._increment_cursor() 
            return Token_Type.EQUAL_EQUAL, err

         return Token_Type.EQUAL, err
      elif current_text == '>':
         if self._peek() == '=':
            self._increment_cursor() 
            return Token_Type.GREATER_EQUAL, err

         return Token_Type.GREATER, err
      elif current_text == '<':
         if self._peek() == '=':
            self._increment_cursor() 
            return Token_Type.LESS_EQUAL, err

         return Token_Type.LESS, err
      elif current_text == '\n':
         self.line_num += 1
         return None, err
      elif current_text == ' ':
         return None, err
      elif current_text == _:
         return None, Lox_Err(msg=f'{self._current_text()} is not a valid token', line_num=self.line_num)

   def _get_number_token(self):
      err = None
      while (next_char := self._peek()) and next_char.isdigit():
         self._increment_cursor()

      if self._peek() == '.':
         self._increment_cursor()
         while (next_char := self._peek()) and next_char.isdigit():
            self._increment_cursor()

      return Token_Type.NUMBER, err





