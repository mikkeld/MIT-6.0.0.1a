# Count vowels

import sys

string = sys.argv[1]
#
# vowels = ['a', 'e', 'i', 'o', 'u']
# count = 0
# for char in list(vowels):
#     if vowels.index(char):
#         count += 1
#
# print 'Number of vowels: ' + str(count)

# Longest substring in alphabetical order

chars = list(string)
longest_string = ""
for i in range(0, len(chars) - 1, 1):
    current_word = chars[i]
    j = i
    while chars[j+1] >= chars[j] and j < len(chars)-2:
        current_word += chars[j+1]
        j += 1
    if len(current_word) > len(longest_string): longest_string = current_word

print longest_string