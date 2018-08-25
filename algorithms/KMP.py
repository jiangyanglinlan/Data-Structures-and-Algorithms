def compute_temporary_array(pattern):
    '''
    :param pattern: str 
    :return: str
    '''
    pattern_len = len(pattern)
    lps = [i for i in range(0, pattern_len)]
    index = 0
    i = 1
    while i < pattern_len:
        if pattern[i] == pattern[index]:
            lps[i] = index + 1
            index += 1
            i += 1
        else:
            if index != 0:
                index = lps[index-1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp(text, pattern):
    lps = compute_temporary_array(pattern)
    i = 0
    j = 0
    text_len = len(text)
    pattern_len = len(pattern)
    while i < text_len and j < pattern_len:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == pattern_len:
            return i - pattern_len
    return False


print(kmp("abcxabcdabcdabcy", "abcdabcy"))