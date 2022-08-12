def main():
    email_name = {}
    email = str(input("Email: "))
    while email != "":
        name = get_email(email)
        confirmation = str(input(f"Is your name {name}? (Y/N)"))
        if confirmation.upper() != "Y" and confirmation != "":
            name = str(input("Name: "))
        email_name[email] = name
        email = str(input("Email: "))

    for email, name in email_name.items():
        print(f"{name} ({email})")

def get_email(email):
    at = email.split("@")[0]
    parts = at.split(".")
    name = " ".join(parts).title()
    return name

if __name__ == '__main__':
    main()