from validator_collection import validators

def main():
        print(validation(input('What\'s your email address? ')))


def validation(email):
    return 'Valid' if validators.email(email) else 'Invalid'


if __name__ == '__main__':
    main()


# we can also implement the program like this below

from validator_collection import validators

def main():
        email = input('What\'s your email address? ')
        try:
                emailIsValid = validators.email(email)
                print("Valid")
        except:
                print("Invalid")
                
if __name__ == '__main__':
    main()

