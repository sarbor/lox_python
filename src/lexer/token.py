from dataclasses import dataclass
from lexer.token_types import Token_Type

@dataclass
class Token:
   token_type: Token_Type
   lexeme: str
   line_num: int
   literal: object
