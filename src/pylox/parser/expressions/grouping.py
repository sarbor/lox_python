from pylox.parser.expressions.expression import Expression
from pylox.parser.visitors.visitor import Visitor

class Grouping(Expression):
   def __init__(self, expression: Expression) -> None:
       self.expression = expression
       
   def accept(self, v: Visitor):
      return v.visit_grouping(self)