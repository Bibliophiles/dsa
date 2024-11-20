def caesarCipher(s, k):
     k %= 26  # Normalize shift to within alphabet range
     result = []

     for char in s:
        if 'a' <= char <= 'z':  # Lowercase letter
            shifted_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result.append(shifted_char)
        elif 'A' <= char <= 'Z':  # Uppercase letter
            shifted_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result.append(shifted_char)
        else:
            # If it's a hyphen or any other character, keep it unchanged
            result.append(char)

     return ''.join(result)





def caesarCipher(s, k):
    k %= 26
    return ''.join(
        chr((ord(char) - base + k) % 26 + base) if 'a' <= char <= 'z' or 'A' <= char <= 'Z' else char
        for char in s
        for base in (ord('a') if 'a' <= char <= 'z' else ord('A'),)
    )
