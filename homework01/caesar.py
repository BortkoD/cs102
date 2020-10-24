import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    ln=len(plaintext)
    for i in range(0, ln):
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


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    ln=len(ciphertext)
    for i in range(0, ln):
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


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
