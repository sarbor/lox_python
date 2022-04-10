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
      self.reserved_keywords = self._initialize_reserved_keywords()

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
      elif token_type == Token_Type.STRING:
         #remove starting and ending quotes
         lexeme = self.source[self.start+1:self.current]
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
      elif current_text.isalpha():
         return self._get_identifier_token()
      elif current_text == '\"':
         return self._get_string_token()
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
      else:
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

   def _get_identifier_token(self):
      err = None

      while (next_char := self._peek()) and next_char.isalpha():
         if next_char == '\n':
            self.line_num += 1
         self._increment_cursor()

      if self._current_text() in self.reserved_keywords:
         return self.reserved_keywords[self._current_text()], err

      return Token_Type.IDENTIFIER, err

   def _get_string_token(self):
      err = None

      while (next_char := self._peek()) and next_char != '\"':
         if next_char == '\n':
            self.line_num += 1
         self._increment_cursor()

      #cant find closing quote
      if self._peek() is None:
         return None, Lox_Err(f'Unterminated string literal', self.line_num)
      
      #moves past the closing quote
      self._increment_cursor()

      return Token_Type.STRING, err


   def _initialize_reserved_keywords(self):
      reserved_keyword_to_token_type = dict()
      reserved_keyword_to_token_type['and'] = Token_Type.AND
      reserved_keyword_to_token_type['class'] = Token_Type.CLASS
      reserved_keyword_to_token_type['else'] = Token_Type.ELSE
      reserved_keyword_to_token_type['false'] = Token_Type.FALSE
      reserved_keyword_to_token_type['for'] = Token_Type.FOR
      reserved_keyword_to_token_type['fun'] = Token_Type.FUN
      reserved_keyword_to_token_type['if'] = Token_Type.IF
      reserved_keyword_to_token_type['nil'] = Token_Type.NIL
      reserved_keyword_to_token_type['or'] = Token_Type.OR
      reserved_keyword_to_token_type['print'] = Token_Type.PRINT
      reserved_keyword_to_token_type['return'] = Token_Type.RETURN
      reserved_keyword_to_token_type['super'] = Token_Type.SUPER
      reserved_keyword_to_token_type['this'] = Token_Type.THIS
      reserved_keyword_to_token_type['true'] = Token_Type.TRUE
      reserved_keyword_to_token_type['var'] = Token_Type.VAR
      reserved_keyword_to_token_type['while'] = Token_Type.WHILE

      return reserved_keyword_to_token_type




