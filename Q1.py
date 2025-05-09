def shift_char(c, shift, is_upper):
    base = ord('A') if is_upper else ord('a')
    return chr((ord(c) - base + shift) % 26 + base)

def encrypt(text, n, m):
    result = []
    markers = [] 
    for c in text:
        if c.islower():
            if ord(c) - ord('a') < 13:
                result.append(shift_char(c, n * m, False))
                markers.append('1')
            else:
                result.append(shift_char(c, -(n + m), False))
                markers.append('2')
        elif c.isupper():
            if ord(c) - ord('A') < 13:
                result.append(shift_char(c, -n, True))
                markers.append('1')
            else:
                result.append(shift_char(c, m ** 2, True))
                markers.append('2')
        else:
            result.append(c)
            markers.append('0')
    return ''.join(result), ''.join(markers)

def decrypt(text, n, m, markers):
    result = []
    for c, mark in zip(text, markers):
        if mark == '1':
            if c.islower():
                result.append(shift_char(c, -(n * m), False))
            elif c.isupper():
                result.append(shift_char(c, n, True))
            else:
                result.append(c)
        elif mark == '2':
            if c.islower():
                result.append(shift_char(c, n + m, False))
            elif c.isupper():
                result.append(shift_char(c, -(m ** 2), True))
            else:
                result.append(c)
        else:
            result.append(c)
    return ''.join(result)

def check_correctness(original, decrypted):
    original_clean = original.strip().replace('\r\n', '\n')
    decrypted_clean = decrypted.strip().replace('\r\n', '\n')

    if original_clean != decrypted_clean:
        print("\n❌ Text mismatch detected! Showing first difference:")
        for i, (o, d) in enumerate(zip(original_clean, decrypted_clean)):
            if o != d:
                print(f"Index {i}: Original='{o}' ({ord(o)}) | Decrypted='{d}' ({ord(d)})")
                break
    return original_clean == decrypted_clean

def main():
    try:
        n = int(input("Enter value for n: "))
        m = int(input("Enter value for m: "))
    except ValueError:
        print("❌ Invalid input. Please enter integers for n and m.")
        return

    try:
        with open("raw_text.txt", "r", encoding="utf-8") as f:
            original_text = f.read()
    except FileNotFoundError:
        print("❌ raw_text.txt not found.")
        return

    encrypted_text, markers = encrypt(original_text, n, m)
    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted_text)
    with open("marker.txt", "w", encoding="utf-8") as f:
        f.write(markers)
    print("✅ Encrypted text written to encrypted_text.txt")

    with open("marker.txt", "r", encoding="utf-8") as f:
        markers = f.read()

    decrypted_text = decrypt(encrypted_text, n, m, markers)
    if check_correctness(original_text, decrypted_text):
        print("✅ Decryption successful — original and decrypted texts match.")
    else:
        print("❌ Decryption failed — texts do not match.")

if __name__ == "__main__":
    main()

