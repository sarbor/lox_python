from ast import Expression

from pylox.parser.expressions.expression import Expression
from pylox.lexer.token import Token

class Binary(Expression):
   def __init__(self, left: Expression, operator: Token, right: Expression):
      self.left = left
      self.operator = operator
      self.right = right

   def accept(self, v):
      return v.visit_binary(self)

   
