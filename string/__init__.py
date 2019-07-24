

# String algorithms

# 1: Revert a string

#########################################################################################################


def iterative_revert(s):
    i = 0
    j = len(s) - 1
    result = [c for c in s]
    while i < j:
        print(i, j)
        result[i], result[j] = result[j], result[i]
        i += 1
        j -= 1
    print(''.join(result))
    print(s)


def recursive_revert(s):
    if len(s) == 0:
        return s

    return recursive_revert(s[1:]) + s[0]


# 1: Revert a string
print(recursive_revert('banana'))
print(iterative_revert('banana'))


#########################################################################################################

# 2 Check anagrams

# Example: silent and listen are anagrams
# Maybe sort both string and then check char by char, but it would be O(n log n) because of the sorting algorithm
# Use an additional data structure to count characters

#########################################################################################################


def check_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_count = {}
    for c in s1:
        if c not in s1_count:
            s1_count[c] = 1
        else:
            s1_count[c] += 1

    for c in s2:
        if c not in s1_count:
            return False
        else:
            s1_count[c] -= 1

    return not any(s1_count.values())


print(check_anagrams('pata', 'tapa'))
print(check_anagrams('pata', 'tapas'))
print(check_anagrams('patas', 'tapas'))
print(check_anagrams('aa', 'aa'))


#########################################################################################################

# 3 Check palindrome

#########################################################################################################


def check_palindrome(s1):

    i = 0
    j = len(s1) - 1
    while i < j:
        if s1[i] != s1[j]:
            return False
        i += 1
        j -= 1

    return True


print(check_palindrome('civic'))
print(check_palindrome('civica'))
print(check_palindrome('a'))
print(check_palindrome('aaa'))


#########################################################################################################

# 4 check balanced parenthesis

#########################################################################################################


brackets = {
    '}': '{',
    ')': '(',
    ']': '['
}


def is_balanced(s):
    stack = []
    for c in s:
        if c in ['(', '{', '[']:
            stack.insert(0, c)
        elif c in [')', '}', ']']:
            expected_brackert = brackets[c]
            if stack.pop(0) != expected_brackert:
                return False

    return len(stack) == 0


expression = "{({()})}"
print(is_balanced(expression))

expression = "{({(})}"
print(is_balanced(expression))

expression = "(())"
print(is_balanced(expression))

expression = ""
print(is_balanced(expression))

expression = "{{"
print(is_balanced(expression))

expression = "({}({}))()()({(())}{{[]}{}[]((([[[][([][[]{}(()())()][][({})][]{}[]()[](()){})]]])))})"
print(is_balanced(expression))


#########################################################################################################

# 5) permutations of a string + dice permutations
# handle combinations with set

#########################################################################################################


def print_permutations(s):
    permutations = [s[0]]
    i = 1
    while i < len(s):
        new_permutations = []
        for element in permutations:
            for j in range(i + 1):
                new_string = [c for c in element]
                new_string.insert(j, s[i])
                new_permutations.append(''.join(new_string))

        permutations = set(new_permutations)
        i += 1
    return permutations


print(print_permutations('aaabb'))


def to_string(values):

    return ''.join(values)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.

def permute(s, start, length):
    if start == length:
        print(to_string(s))
    else:
        for i in range(start, length + 1):
            s[start], s[i] = s[i], s[start]
            print('permute ' + str(start) + ',' + str(i) + ' : ' + str(s))
            permute(s, start + 1, length)
            s[start], s[i] = s[i], s[start]  # backtrack


# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1)


#########################################################################################################
