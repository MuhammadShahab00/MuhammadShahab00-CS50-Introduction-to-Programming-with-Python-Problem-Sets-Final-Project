import re

def main():
    while True:
        print(count(input('Text: ')))


def count(s):
    um_list = re.findall(r'\b\W*um\b\W*', s, re.MULTILINE | re.IGNORECASE)
    return len(um_list)

if __name__ == '__main__':
    main()
