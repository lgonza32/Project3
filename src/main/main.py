import random
import string
import time
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
    This function also measure the time it takes to run the algorithm
    in nanoseconds (ns).
    """
    # s1 = "mangoes"
    # s2 = "mementos"
    # Accept two strings as input from the user
    n1 = int(input("Enter the size (n1) of s1: "))
    n2 = int(input("Enter the size (n2) of s2: "))
    
    # Generate random strings of n size
    s1 = generate_random_string(n1)
    s2 = generate_random_string(n2)
    
    start_time = time.time_ns()  # Get the current time in nanoseconds
    lcs, lcs_length = get_lcs(s1, s2)
    lcs_str = lcs_string(s1, s2, lcs)
    end_time = time.time_ns()  # Get the end time in nanoseconds
    
    # Calculate the elapsed time in nanoseconds
    duration_ns = end_time - start_time
    
    # Results
    print(f"s1: {s1}")
    print(f"s2: {s2}")
    print(f"LCS length: {lcs_length}")
    print(f"Longest Common Subsequence: {lcs_str}")
    print(f"Time (ns): {duration_ns}")
    
# Run the main function
if __name__ == "__main__":
    main()