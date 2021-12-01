from enum import Enum

class Token_Type(Enum):
   LEFT_PAREN = '('
   RIGHT_PAREN = ')'
   LEFT_BRACE = '{'
   RIGHT_BRACE = '}'
   COMMA = ','
   DOT = '.'
   MINUS = '-'
   PLUS = '+'
   SEMICOLON = ';'
   SLASH = '/'
   STAR = '*'

   BANG = '!'
   NOT_EQUAL = '!='
   EQUAL = '='
   EQUAL_EQUAL = '=='
   GREATER = '>'
   GREATER_EQUAL = '>='
   LESS = '<'
   LESS_EQUAL = '<='

   #types
   IDENTIFIER = 1
   STRING = 2
   NUMBER = 3

   #keywords
   AND = 4
   CLASS = 5
   ELSE = 6
   FALSE = 7
   FUN = 8
   FOR = 9
   IF = 10
   NIL = 11
   OR = 12
   PRINT = 13
   RETURN = 14
   SUPER = 15
   THIS = 16
   TRUE = 17
   VAR = 18
   WHILE = 19

   EOF = 20



