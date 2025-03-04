from anagram import areAnagrams

def test_anagrams():
    assert areAnagrams("anagram", "nagaram") == True
    assert areAnagrams("below", "elbow") == True
    assert areAnagrams("study", "dusty") == True
    assert areAnagrams("night", "thing") == True
    assert areAnagrams("act", "cat") == True

def test_anagrams_len_not_equal():
    assert areAnagrams ("anagram", "nagra") == False
    assert areAnagrams ("cat", "action") == False

def test_anagrams_empty_string():
    assert areAnagrams("", "") == True

def test_anagrams_equal_len_diff_count_letters():
    assert areAnagrams("anagram", "nagarm") == False
    assert areAnagrams("anagram", "nagarama") == False

