def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            print(f"Pattern found at index {i}")

naive_string_match("ABABDABACDABABCABAB", "ABABCABAB")