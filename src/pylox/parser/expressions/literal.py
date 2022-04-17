from pylox.parser.expressions.expression import Expression
from pylox.parser.visitors.visitor import Visitor

class Literal(Expression):
   def __init__(self, value: str) -> None:
      self.value = value
       
   def accept(self, v: Visitor):
      return v.visit_literal(self)