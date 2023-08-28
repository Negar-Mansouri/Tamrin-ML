
Q7

from collections import Counter

numbers_list = [
    [1, 3, 2, 1, 5],
    [1, 4, 5, 2, 4],
    [2, 3, 2, 4, 5],
    [5, 4, 3, 2, 3],
    [3, 2, 3, 4, 5]
]

flat_numbers = [num for row in numbers_list for num in row]

number_counts = Counter(flat_numbers)

most_common_numbers = number_counts.most_common(3)

print("The three most common numbers:")
for num, count in most_common_numbers:
    print(f"Number: {num}, Count: {count}")
    
    
    
    
    
    
    
    
Q-13

def find_matching_strings(pattern, string_list):
    matching_strings = []

    pattern_dict = {i: pattern[i] for i in range(len(pattern)) if pattern[i] != '*'}

    for string in string_list:
        if len(string) != len(pattern):
            continue

        is_match = True

        for index, char in pattern_dict.items():
            if string[index] != char:
                is_match = False
                break

        if is_match:
            matching_strings.append(string)

    return matching_strings


L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']

user_pattern = input("Enter the pattern with asterisks (*): ")

matching_strings = find_matching_strings(user_pattern, L)

print("Matching strings:")
for string in matching_strings:
    print(string)
    
    
    

Q-14

data = [
    {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}
]

print("Users whose phone number ends in an 8:")
for user in data:
    if user['phone'].endswith('8'):
        print(user['name'])

print("\nUsers without an email address listed:")
for user in data:
    if not user['email']:
        print(user['name'])
        
        
        

Q-11(126)

def is_real_word(word, word_list):
    return word in word_list

myWords = ['cow', 'cat', 'pig', 'man', 'woman']
user_word = input("Enter a word: ").strip()

if is_real_word(user_word, myWords):
    print(f"{user_word} is a real word!")
else:
    print(f"{user_word} is not a real word.")
    
    
    
