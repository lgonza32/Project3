from lcs import *

def main():
    """
    The main function that helps demonstrate the implementation of
    the Longest Common Sequence (LCS) algorithm between two strings.
    """
    s1 = "mangoes"
    s2 = "mementos"
    
    lcs, lcs_length = get_lcs(s1, s2)
    lcs_str = lcs_string(s1, s2, lcs)
    
    # Results
    print(f"LCS Length: {lcs_length}")
    print(f"Longest Common Subsequence: {lcs_str}")
    
# Run the main function
if __name__ == "__main__":
    main()