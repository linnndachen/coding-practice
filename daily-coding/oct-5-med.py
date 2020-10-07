"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string 'de' and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

def func(strings, prefix='s'):
    res = []
    length = len(prefix)
    for string in strings:
        if string[:length] == prefix:
            res.append(string)

    return res

strings = ['spring', 'apple']

print(func(strings=strings, prefix='s'))