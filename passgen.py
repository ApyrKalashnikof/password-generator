import secrets
import string


def main():
    print(make_pass())



def make_pass():
    length = 14 + secrets.randbelow(7)
    password = ""
    source = string.ascii_letters + string.punctuation + string.digits

    for _ in range(length):
        password += secrets.choice(source)
    return password

if __name__ == "__main__":
    main()
