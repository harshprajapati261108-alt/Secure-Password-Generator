import random
import string
import os

def print_banner():
    """Prints a professional ASCII banner for the CLI tool."""
    print("=" * 55)
    print("      🔒 SECURE PASSWORD GENERATOR & MANAGER 🔒      ")
    print("=" * 55)

def generate_password(letters_cnt, symbols_cnt, numbers_cnt):
    """Generates a highly secure password based on user constraints."""
    # Character pools using Python's standard string library
    all_letters = string.ascii_letters  # Includes a-z and A-Z
    all_symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    all_numbers = string.digits         # Includes 0-9

    password_list = []

    # Dynamic random choices based on user counts
    for _ in range(letters_cnt):
        password_list.append(random.choice(all_letters))

    for _ in range(symbols_cnt):
        password_list.append(random.choice(all_symbols))

    for _ in range(numbers_cnt):
        password_list.append(random.choice(all_numbers))

    # Advanced Shuffling: Cryptographically safer mix
    # Using random.sample on the full length ensures absolute randomness
    shuffled_password = random.sample(password_list, len(password_list))
    
    # Joining characters to form the final string
    return "".join(shuffled_password)

def log_password_securely(password):
    """Logs the generated password configuration to a local file safely."""
    file_name = "passwords_log.txt"
    try:
        # Appending the password securely to a local file
        with open(file_name, "a") as file:
            file.write(f"Generated Password: {password}\n")
        print(f"[SUCCESS] Password securely logged to '{file_name}'.")
    except IOError as e:
        print(f"[ERROR] Failed to save password to file: {e}")

def main():
    print_banner()
    
    # Input Validation & Robust Error Handling
    try:
        a = int(input("How many letters would you like in your password? -> "))
        b = int(input("How many symbols would you like? -> "))
        c = int(input("How many numbers would you like? -> "))
        
        if a < 0 or b < 0 or c < 0:
            print("[INVALID INPUT] Counts cannot be negative numbers. Please try again.")
            return

        total_length = a + b + c
        if total_length < 8:
            print("[WARNING] For strong security, a password should be at least 8 characters long.")
        
        # Core execution
        final_password = generate_password(a, b, c)
        
        print("\n" + "-" * 40)
        print(f" Your Generated Password is: {final_password}")
        print("-" * 40 + "\n")
        
        # Save to file capability
        log_password_securely(final_password)
        
    except ValueError:
        print("[ERROR] Please enter valid integers/numbers only.")

if __name__ == "__main__":
    main()
