import random
import string
from lcs import *

def generate_random_string(n):
    """
    Generates a random string of the given length using 
    lowercase letters and digits.
    
    Args:
        n (int (size)): The size of the string wanted.

    Returns:
        string: a random string of n size.
    """
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=n))

def main():
    """
    The main function that helps demonstrate the implementation of
    the Longest Common Sequence (LCS) algorithm between two strings.
    """
    # s1 = "mangoes"
    # s2 = "mementos"
    # Accept two strings as input from the user
    n1 = int(input("Enter the size (n1) of s1: "))
    n2 = int(input("Enter the size (n2) of s2: "))
    
    # Generate random strings of n size
    s1 = generate_random_string(n1)
    s2 = generate_random_string(n2)
    
    lcs, lcs_length = get_lcs(s1, s2)
    lcs_str = lcs_string(s1, s2, lcs)
    
    # Results
    print(f"s1: {s1}")
    print(f"s2: {s2}")
    print(f"LCS Length: {lcs_length}")
    print(f"Longest Common Subsequence: {lcs_str}")
    
# Run the main function
if __name__ == "__main__":
    main()