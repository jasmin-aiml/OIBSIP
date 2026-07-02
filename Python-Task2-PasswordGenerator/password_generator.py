# Unique Workspace Implementation
# Evaluation Tracker Identity Module
import random
import string

def construct_custom_keyphrase():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("     DYNAMIC CRYPTO-KEY GEN ARCHITECTURE ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    try:
        user_size_request = input("Enter requested passphrase length (Min 6): ").strip()
        target_length = int(user_size_request)
        
        if target_length < 6:
            print("\n[REJECTED]: Length setting fails basic defense criteria thresholds.")
            return
            
        print("\nSelect component attributes:")
        allow_alpha = input("Utilize alphabetic characters? (y/n): ").strip().lower() == 'y'
        allow_numeric = input("Utilize numerical sequences? (y/n): ").strip().lower() == 'y'
        allow_special = input("Utilize specialized punctuation? (y/n): ").strip().lower() == 'y'
        
        composite_pool = ""
        if allow_alpha:
            composite_pool += string.ascii_letters
        if allow_numeric:
            composite_pool += string.digits
        if allow_special:
            composite_pool += string.punctuation
            
        if not composite_pool:
            print("\n[ALERT]: Zero configuration attributes chosen. Fallback array deployed.")
            composite_pool = string.ascii_letters + string.digits
            
        assembled_keyphrase = "".join(random.choice(composite_pool) for _ in range(target_length))
        
        print("\n=========================================")
        print(f" Generated Keyphrase Sequence: {assembled_keyphrase}")
        print("=========================================")
        
    except ValueError:
        print("\n[MALFORMED DATA]: System requires valid integer metrics for setup.")

if __name__ == "__main__":
    construct_custom_keyphrase()
