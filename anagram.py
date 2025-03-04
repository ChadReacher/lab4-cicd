def areAnagrams(str1, str2):
    if len(str1) == len(str2):
        return False
    return sorted(str1) == sorted(str2)

