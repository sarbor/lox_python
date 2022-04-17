from dataclasses import dataclass
from pylox.lexer.token_types import Token_Type

@dataclass
class Token:
   token_type: Token_Type
   lexeme: str
   line_num: int
   literal: object

   def __repr__(self) -> str:
       return self.lexeme
