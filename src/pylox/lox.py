import sys
from lexer.tokenizer import Tokenizer

class Lox:
   has_err = False

   def report_error(self, line_num, msg):
      self.has_err = True
      print(f'line: {line_num} {msg}', file=sys.stderr)

   def run(self, text):
      tokenizer = Tokenizer()
      tokens = tokenizer.tokenize(text)
      print(tokens)

      if self.has_err:
         sys.exit(1)

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
