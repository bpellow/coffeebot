import sys
from account_generator import AccountGenerator
from driver import create_account

def main():
    if len(sys.argv) < 6 or len(sys.argv) > 7:
        print("Incorrect usage. Please follow this format:")
        print("python coffeebot.py name email_prefix email_domain password duration [--bitwarden]")
        sys.exit(1)
    elif len(sys.argv) == 7 and sys.argv[6] != "--bitwarden":
        print("Incorrect usage. Please follow this format:")
        print("python coffeebot.py name email_prefix email_domain password duration [--bitwarden]")
        sys.exit(1)
    elif sys.argv[5].isnumeric() == False:
        print("Incorrect usage. Please follow this format:")
        print("python coffeebot.py name email_prefix email_domain password duration [--bitwarden]")
        sys.exit(1)
    elif int(sys.argv[5]) > 60:
        print("Duration must be less than 60 days")
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