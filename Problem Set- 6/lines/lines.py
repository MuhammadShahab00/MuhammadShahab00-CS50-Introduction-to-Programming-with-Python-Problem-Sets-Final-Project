import sys

def main():
    check_command_line_arg():
        try:
            file = open(sys.argv[1],"r")
            lines = file.readlines()
        except FileNotFoundError:
            sys.exit('File does not exist')
        count_lines = 0
        for lines in line:
            if check_comment_or_empty_line(lines) == False:
                count_lines +=1
        print(count_lines)

    return lines

def check_command_line_arg():
      if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif sys.argv[1].endswith('.py') == False:
        sys.exit('Not a Python file')
    else:
        print(count_lines(sys.argv[1]))

def check_comment_or_empty_line(line):
    if line.isspace():
        return True
    if lines.lstrip().startswith('#'):
        return True
    return False

if __name__ == '__main__':
    main()
