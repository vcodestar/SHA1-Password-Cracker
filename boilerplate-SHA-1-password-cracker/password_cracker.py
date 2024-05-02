import hashlib

def crack_sha1_hash(hash, use_salts=False):
    password_array = read_passwords_from_file("top-10000-passwords.txt")

    if use_salts:
        salts = read_passwords_from_file("known-salts.txt")
        for salt in salts:
            salt_bytes = salt.encode()  # Convert salt to bytes
            for password in password_array:
                hash1 = hashlib.sha1(salt_bytes + password.encode()).hexdigest()
                hash2 = hashlib.sha1(password.encode() + salt_bytes).hexdigest()
                if hash == hash1:
                    return password
                elif hash == hash2:
                    return password

    for password in password_array:
        hash_attempt = hashlib.sha1(password.encode()).hexdigest()
        if hash == hash_attempt:
            return password

    return "PASSWORD NOT IN DATABASE"

def read_passwords_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []
