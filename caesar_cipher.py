from corpus_loader import word_list, name_list


def encrypt(ptext, key):
    """
    Simple Caesar Cipher encryption tool. Shifts alphabetic characters only. Whitespaces and other characters are not
    shifted.

    :param ptext: (str) Plaintext to encrypt.
    :param key: (int) Number of letters to shift. Negative for left shift, positive for right shift.
    :return: (str) Ciphertext encrypted with given key.
    """
    ctext = ''
    for char in ptext:
        if char.islower():
            ctext += chr(((ord(char) + key - 97) % 26) + 97)
        elif char.isupper():
            ctext += chr(((ord(char) + key - 65) % 26) + 65)
        else:
            ctext += char
    return ctext


def decrypt(ctext, key):
    """
    Simple Caesar Cipher decryption tool. Shifts alphabetic characters only. Assumes whitespaces and other characters
    were not shifted.

    :param ctext: (str) Ciphertext to decrypt.
    :param key: (int) Number of letters shifted to create ciphertext. Negative for left shift, positive for right shift.
    :return: (str) Plaintext decrypted with given key.
    """
    ptext = ''
    for char in ctext:
        if char.islower():
            ptext += chr(((ord(char) - key - 97) % 26) + 97)
        elif char.isupper():
            ptext += chr(((ord(char) - key - 65) % 26) + 65)
        else:
            ptext += char
    return ptext


def crack(ctext, first_match=True, words_to_check=10, match_ratio=0.29):
    """
    Cracks caesar ciphers in which only alphabetic characters ([a-z],[A-Z]) are shifted, using nltk english word and
    name corpus. Checks user defined number of words of cipher against corpus.

    :param ctext: (str) Ciphertext to be cracked.
    :param first_match: (bool) Returns first match found if True. Returns a list of every match found if False.
    :param words_to_check: (int) Number of words to check for validity. If <= 0, checks all words.
    :param match_ratio: (float) Required ratio of word matches to be considered a valid solution.
    :return: (str) Plaintext if first_match is True. (List) Strings of all plaintext solutions if first_match is False.
    """
    solution = []
    for i in range(26):
        ptext = decrypt(ctext, i).split(" ")
        if len(ptext) > words_to_check - 1 and words_to_check > 0:
            check = words_to_check
        else:
            check = len(ptext)
        match = 0
        for word in range(check):
            # Clean the word of non-alpha characters, usually punctuation
            check_word = "".join(j for j in ptext[word] if j.isalpha())
            if check_word in word_list or check_word in name_list:
                match += 1
        if match/check >= match_ratio:
            solution.append(decrypt(ctext, i))
    if first_match:
        if solution:
            return solution[0]
        else:
            return ''
    else:
        return solution
