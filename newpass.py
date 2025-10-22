import secrets
import string

def generate_password():
    # Define character pools
    lowercase = ''.join(c for c in string.ascii_lowercase if c not in 'ilo')
    uppercase = ''.join(c for c in string.ascii_uppercase if c not in 'IO')
    digits = ''.join(c for c in string.digits if c not in '0')

    # Weighted pool: mostly lowercase, few uppercase, few digits
    weighted_pool = (
        lowercase * 7 +
        uppercase * 1 +
        digits * 2
    )

    # Each group has 6 characters, total of 4 groups
    groups = ["".join(secrets.choice(weighted_pool) for _ in range(6)) for _ in range(4)]

    # Join groups with hyphens
    return "-".join(groups)

def main():
    password = generate_password()
    print(password)

if __name__ == "__main__":
    main()
