# Caesar Cipher Tools

This is a suite of tools for python to encrypt, decrypt, and crack alphebetical caesar ciphers. All of the methods assume that only alpha characters are shifted and other characters remain the same. They also assume that capitalization remains the same. The crack tool makes use of the nltk english language words corpus and the nltk names corpus.

## Methods

There are 3 methods contained here:

* encrypt:
  * Simple Caesar Cipher encryption tool. Shifts alphabetic characters only. Whitespaces and other characters are not shifted.
  * Params:
    1. ptext: (str) Plaintext to encrypt.
    2. key: (int) Number of letters to shift. Negative for left shift, positive for right shift.
  * Returns:
    * (str) Ciphertext encrypted with given key.
* decrypt:
  * Simple Caesar Cipher decryption tool. Shifts alphabetic characters only. Whitespaces and other characters are not shifted.
  * Params:
    1. ctext: (str) Ciphertext to dencrypt.
    2. key: (int) Number of letters shifted to create the ciphertext. Negative for left shift, positive for right shift.
  * Returns:
    * (str) Plaintext decrypted with given key.
* crack:
  * Cracks caesar ciphers in which only alphabetic characters ([a-z],[A-Z]) are shifted, using nltk english word and name corpus. Checks user defined number of words of cipher against corpus.
  * Params:
    1. ctext: (str) Ciphertext to be cracked.
    2. first_match: (bool) Returns first match found if True. Returns a list of every match found if False. Default: True
    3. words_to_check: (int) Number of words to check against the corpus for validity. If <= 0, checks all words. Default: 10
    4. match_ratio: (float) Required ratio of word matches to non-matches to be considered a valid solution. Should be between 0 and 1. A match ratio of 0.4 will require 40% or greater of the checked words to be contained in the corpus for a solution to be considered valid. Default: 0.29
  * Returns:
    * (str) Plaintext of the first found possible solution *if first_match == True.*
    * (List) Strings of the plantext of all possible solutions *if first_match == False.*

## Example Usage

* `encrypt("I sure love these caesar cipher tools!", 3)`
  * returns `"L vxuh oryh wkhvh fdhvdu flskhu wrrov!"`
* `decrypt("L vxuh oryh wkhvh fdhvdu flskhu wrrov!", 3)`
  * returns `"I sure love these caesar cipher tools!"`
* `crack("Hvsfs'g bc kom gcaspcrm qcizr twuifs cih hvwg gsqfsh asggous kwhvcih gcas gcfh ct qccz dmhvcb gqfwdh!")`
  * returns `"There's no way somebody could figure out this secret message without some sort of cool python script!"`
