def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]
    for string in strings[1:]:

        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

strings = ["apple", "application", "aptitude"]
common_prefix = longest_common_prefix(strings)
print("Longest common prefix:", common_prefix)