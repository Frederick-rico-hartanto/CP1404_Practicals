MIN_LENGTH = 4




def main():
    password = input(f"Enter a password which consist of at least {MIN_LENGTH} characters: ")
    is_valid_password(password, MIN_LENGTH)
    print("Password is saved")


def is_valid_password(password,MIN_LENGTH):
    while len(password) < MIN_LENGTH:
        print("Password is too short: ")
        password = input(f"Enter a password which consist of at least {MIN_LENGTH} characters: ")


def asterisks():
    password = get_pass(MIN_LENGTH)
    print_asterisk_pass(password)

def get_pass(MIN_LENGTH):
    password = input(f"Enter a password which consist of at least {MIN_LENGTH} characters: ")
    while len(password) < MIN_LENGTH:
        print("Password too short")
        password = input(f"Enter password of at least {MIN_LENGTH} characters: ")

    return '*' * len(password)

def print_asterisk_pass(sequence):
    print('*' * len(sequence))

# asterisks()
main()