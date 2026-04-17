# Leruo Phiri 2868956

This is my Lab Repository
Bugs found:

index for getCols did not increase. Solution: Made use of enumerate to go through the columns

index for the current best student/ mark is not set to the current student within the loop when the mark is better than the current best Solution: Assigned the best_idx to the current best

Testing Notes made:

Initially i started with 2 test files but due to how small the getBest program is. I decided to use one test file and categorize which methods I was testing using comments

I focused on checking for the normal boundaries, and edge cases such as first and last mark for the findTop

I made sure to have the file closed after being used within getbest.py
