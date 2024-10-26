<!-- DESCRIPTION -->
# Project 3 - Longest Common Sequence

A program that computes the Longest Common Sequence of any given two strings of sizes n_1 and n_2

<!-- REQUIREMENTS -->
## Requirements
- Minimum Python version 3.9.2
- Minimum PyTest version 8.3.3

<!-- INSTALLATION -->
## How to Install
1. Clone Repo: 
```sh
git clone https://github.com/lgonza32/Project3
```
2. Navigate to directory
4. Run program

<!-- USAGE -->
## Usage
To run this program, simply execute the `main.py` file. Note that within `main.java`, there are commented out lines where it prints out the LCS. If you want to see the LCS, uncomment those lines. I commented them out so I can just see the output of experimental result in nanoseconds without the hassle of seeing large sized strings.

### Input:
- Users are able to input each sizes of each string, s1 and s2

### Output:
- The program will either output randomly generated strings of size n, the LCS of the two strings, and/or the runtime of the program in nanoseconds.

### Example:
```sh
Enter the size (n1) of s1: 30
Enter the size (n2) of s2: 30
s1: 5qqik4rqn5v5t6br7o8plhxo4p69ae
s2: ro2wtjp5xrs3wigv6kcf1dfo2kiidx
LCS length: 6
Longest Common Subsequence: r5v6ox
Experimental Results (ns): 999800
```

<!-- PROGRAM STRUCTURE -->
## Program Structure
- main.py: Contains main function of input and output of program.
- lcs.py: Contains the lcs implementation.

<!-- TIME COMPLEXITY -->
## Time Complexity
Overall time complexity of the program is O(n_1 * n_2)
Theoretical analysis of the Time Complexity is stated within the submitted document.
