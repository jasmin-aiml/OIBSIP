import random
import string

def construct_custom_keyphrase():
    print("===================================================")
    print("     DYNAMIC CRYPTO-KEY PASSPHRASE GENERATOR       ")
    print("===================================================\n")
    
    try:
        total_characters = int(input("Specify target passphrase character length: "))
        if total_characters < 4:
            print("❌ Security warning: Passphrase must be at least 4 characters long.")
            return
    except ValueError:
        print("❌ Technical execution failure: Numeric integer value expected.")
        return

    include_uppercase = input("Integrate uppercase alphabetic registers? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Integrate numeric data integers? (y/n): ").strip().lower() == 'y'
    include_specials = input("Integrate specialized ascii punctuation elements? (y/n): ").strip().lower() == 'y'

    character_pool = string.ascii_lowercase
    guaranteed_elements = [random.choice(string.ascii_lowercase)]

    if include_uppercase:
        character_pool += string.ascii_uppercase
        guaranteed_elements.append(random.choice(string.ascii_uppercase))
    if include_numbers:
        character_pool += string.digits
        guaranteed_elements.append(random.choice(string.digits))
    if include_specials:
        character_pool += string.punctuation
        guaranteed_elements.append(random.choice(string.punctuation))

    if len(guaranteed_elements) > total_characters:
        print("❌ Logical matrix contradiction: Length configuration threshold too low.")
        return

    rem_length = total_characters - len(guaranteed_elements)
    random_compilation = [random.choice(character_pool) for _ in range(rem_length)]
    
    secure_matrix = guaranteed_elements + random_compilation
    random.shuffle(secure_matrix)
    generated_keyphrase = "".join(secure_matrix)

    print("\n---------------------------------------------------")
    print(f"🔒 SECURE GENERATED PASSPHRASE: {generated_keyphrase}")
    print("---------------------------------------------------")

if __name__ == "__main__":
    construct_custom_keyphrase()
