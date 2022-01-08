from pylox.lexer.token import Token 
from typing import List, Optional
from pylox.lexer.token_types import Token_Type

class Tokenizer:
   def __init__(self):
      self.tokens = []
      self.source = ""
      self.current = 0
      self.start = 0
      self.line_num = 1

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
      self._add_source(text)

      while not self._at_end():
         token_type = self.scan_token_type()
         if token_type:
            self._add_token(token_type)

         self._increment_cursor()
         self.start = self.current

      self._add_token(Token_Type.EOF)

      return self.tokens

   def _at_end(self) -> bool:
      return self.current >= len(self.source) 

   def _increment_cursor(self) -> None:
      self.current += 1

   def _decrement_cursor(self) -> None:
      self.current -= 1

   def _peek(self) -> Optional[str]:
      #checks if cursor is at last character
      next_text = None
      self._increment_cursor()
      if not self._at_end():
         next_text = self.source[self.current]
      self._decrement_cursor()
      return next_text

   def scan_token_type(self) -> Token_Type:
      current_text = self._current_text()

      match current_text:
         case '(':
            return Token_Type.LEFT_PAREN
         case ')':
            return Token_Type.RIGHT_PAREN
         case '{':
            return Token_Type.LEFT_BRACE
         case '}':
            return Token_Type.RIGHT_BRACE
         case ',':
            return Token_Type.COMMA
         case '.':
            return Token_Type.DOT
         case '-':
            return Token_Type.MINUS
         case '+':
            return Token_Type.PLUS
         case ';':
            return Token_Type.SEMICOLON
         case '/':
            if self._peek() == '/':
               while (next_char := self._peek()) != '\n' and next_char:
                  self._increment_cursor()

               return None
            return Token_Type.SLASH
         case '*':
            return Token_Type.STAR
         case '!':
            if self._peek() == '=':
               self._increment_cursor() 
               return Token_Type.NOT_EQUAL

            return Token_Type.BANG
         case '=':
            if self._peek() == '=':
               self._increment_cursor() 
               return Token_Type.EQUAL_EQUAL

            return Token_Type.EQUAL
         case '>':
            if self._peek() == '=':
               self._increment_cursor() 
               return Token_Type.GREATER_EQUAL

            return Token_Type.GREATER
         case '<':
            if self._peek() == '=':
               self._increment_cursor() 
               return Token_Type.LESS_EQUAL

            return Token_Type.LESS
         case '\n':
            self.line_num += 1
         case ' ':
            return None
         case _:
            raise ValueError(f'{self._current_text()} is not a valid token')



