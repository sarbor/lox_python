import sys
from pylox.lexer.tokenizer import Tokenizer
from pylox.err import Lox_Err
class Lox:
   def run(self, text):
      tokenizer = Tokenizer()
      tokens, err = tokenizer.tokenize(text)

      if err:
         err.report_error()

   def run_lox_file(self, filename):
      with open(filename) as program:
         lines = program.read_lines()
         self.run(lines)

   def lox_repl(self):
      text = input("> ")
      
      while len(text):
         self.run(text)
         text = input("> ")


def main():
   argc = len(sys.argv)
   lox = Lox()

   if argc == 2:
      lox_program_name = sys.argv[1]
      lox.run_lox_file(lox_program_name)
   elif argc == 1:
      lox.lox_repl()
   else:
      raise ValueError("Incorrect number of CL Args")


if __name__ == '__main__':
   main()
