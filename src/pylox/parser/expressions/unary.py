from pylox.lexer.token import Token
from pylox.parser.expressions.expression import Expression
from pylox.parser.visitors.visitor import Visitor

class Unary(Expression):
   def __init__(self, operator: Token, expression: Expression) -> None:
       self.operator = operator
       self.expression = expression

   def accept(self, v: Visitor):
      return v.visit_unary(self)