import sys
from account_generator import AccountGenerator
from bot import create_account

#inputs are name, email_prefix, email_domain, password, duration
def main():
    if len(sys.argv) < 6 or len(sys.argv) > 7:
        print("Incorrect usage. Please follow this format:")
        print("python coffeebot.py name email_prefix email_domain password duration [--bitwarden]")
        sys.exit(1)

    args = sys.argv[1:6]
    generator = AccountGenerator(*args)
    data = generator.generate_accounts()
    for row in data:
        create_account(*row)
    if "--bitwarden" in sys.argv:
        generator.store_details()
    

if __name__ == "__main__":
    main()