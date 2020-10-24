def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    ln = len(plaintext)
    key_len = len(keyword)
    for i in range(0, ln):
        if ord('A') <= ord(keyword[i%key_len]) <= ord('Z'):
            shift=ord(keyword[i%key_len])-ord('A')
        else:
            shift=ord(keyword[i%key_len])-ord('a')
        if ord('Z') >= ord(plaintext[i]) >= ord('A'):
            if ord(plaintext[i])+shift <= ord('Z'):
                ciphertext=ciphertext + chr(ord(plaintext[i])+shift)
            else:
                ciphertext=ciphertext + chr(ord('A')+ord(plaintext[i])+shift-ord('Z')-1)
        elif ord('z') >= ord(plaintext[i]) >= ord('a'):
            if ord(plaintext[i])+shift <= ord('z'):
                ciphertext=ciphertext + chr(ord(plaintext[i])+shift)
            else:
                ciphertext=ciphertext + chr(ord('a')+ord(plaintext[i])+shift-ord('z')-1)
        else:
            ciphertext=ciphertext + plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    ln = len(ciphertext)
    key_len = len(keyword)
    for i in range(0, ln):
        if ord('A') <= ord(keyword[i%key_len]) <= ord('Z'):
            shift=ord(keyword[i%key_len])-ord('A')
        else:
            shift=ord(keyword[i%key_len])-ord('a')
        if ord('Z') >= ord(ciphertext[i]) >= ord('A'):
            if ord(ciphertext[i])-shift >= ord('A'):
                plaintext=plaintext + chr(ord(ciphertext[i])-shift)
            else:
                plaintext=plaintext + chr(ord('Z')-ord('A')+ord(ciphertext[i])-shift+1)
        elif ord('z') >= ord(ciphertext[i]) >= ord('a'):
            if ord(ciphertext[i])-shift >= ord('a'):
                plaintext=plaintext + chr(ord(ciphertext[i])-shift)
            else:
                plaintext=plaintext + chr(ord('z')-ord('a')+ord(ciphertext[i])-shift+1)
        else:
            plaintext=plaintext + ciphertext[i]
    return plaintext
