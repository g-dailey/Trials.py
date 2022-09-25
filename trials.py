"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)



def get_all_evens(nums):

    even_nums = []

    for num in nums:
        if num %2 == 0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    result = []
    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])
    return result


def print_as_numbered_list(items):

    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):

    nums = []
    num_start = start
    # num_stop = stop - 1

    # for num in range(start, stop):
    #     nums.append(num)
    # return nums

    while num_start < stop:
        nums.append(num_start)
        num_start += 1
    return nums

print(get_range(0,5))

def censor_vowels(word):

    char = []

    for letter in word:
        if letter in 'aeiou':
            char.append('*')
        else:
            char.append(letter)
    return ''.join(char)

print(censor_vowels("hello world"))





def snake_to_camel(string):
    camel_case = []
    split_string = string.split('_')
    # print(split_string)

    for word in split_string:
        camel_case.append(f'{word[0].upper()}{word[1:]}')
        #adding a comment

    return "".join(camel_case)

# print(snake_to_camel('hello_world'))




def longest_word_length(words):

    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

# print(longest_word_length(['jellyfish', 'zebra', 'nhskjfhghdfhhvdg']))




def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return ''.join(result)

# print(truncate('hi***!!!! wooow'))



def has_balanced_parens(string):

    parens = 0

    for char in string:
        if char == '(':
            parens +=1
        elif char == ")":
            parens -=1

        if parens != 0:
            return False

    return parens == 0
# print(has_balanced_parens("(()))("))

def compress(string):
    compressed = []
    current_char = ''
    char_count = 0

    for char in string:
        if char != current_char:
            compressed.append(current_char)
            if char_count > 1:
                compressed.append(str(char_count))
            current_char = char
            char_count = 0
        char_count+=1
    compressed.append(current_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)

# print(compress('aabbaabb'))
