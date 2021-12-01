from lexer.token import Token 
from typing import List
from lexer.token_types import Token_Type

class Tokenizer:
   def __init__(self, source: str):
      self.tokens = []
      self.source = source
      self.current = 0
      self.start = 0
      self.line_num = 1

   def _current_text(self) -> str:
      return self.source[self.current]

   def _add_token(self, token_type: Token_Type) -> None:
      if token_type == Token_Type.EOF:
         lexeme = ''
      else:
         lexeme = self._current_text()

      token = Token(token_type, lexeme, self.line_num, None)
      self.tokens.append(token)

   def tokenize(self) -> List[Token]:
      while self.not_at_end():
         token_type = self.scan_token_type()
         if token_type:
            self._add_token(token_type)
         self.next()

      self._add_token(Token_Type.EOF)

      return self.tokens

   def not_at_end(self) -> bool:
      return self.current < len(self.source)

   def next(self):
      self.current += 1


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
            return Token_Type.SLASH
         case '*':
            return Token_Type.STAR
         case '\n':
            self.line_num += 1
         case ' ':
            self.next()
            self.scan_token_type()
         case '':
            return None
         case _:
            raise ValueError(f'{current_text} is not a valid token')



