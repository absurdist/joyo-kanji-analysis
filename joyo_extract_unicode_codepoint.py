import sys
import os

import codecs

def main():
  #filepath = sys.argv[1]
  input_file_path = './joyo-kanji-code-u.csv'

  print(input_file_path)

  if not os.path.isfile(input_file_path):
    print("File path {} does not exist. Exiting...".format(input_file_path))
    sys.exit()

  with codecs.open(input_file_path, encoding='utf-8') as f:
    count = 0
    for line in f:
      count += 1

      is_character, char, code_point = parse_input_line(line)

      if (is_character):
        print("line {} character {} code point {} contents {}".format(count, char, code_point, line))

  f.close()

def parse_input_line(line):

  is_character = True
  char = 'x'
  code_point = 1

  return is_character, char, code_point

if __name__ == '__main__':
  main()
