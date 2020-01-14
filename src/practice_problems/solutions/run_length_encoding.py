"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded
have no digits and consists solely of alphabetic characters. You can assume the string
to be decoded is valid.
"""


def encode_run_length(string):
    """I'm aware this is a dirty solution."""
    encoded = ""
    count = 1
    for char, next_char in zip(string, string[1:] + "\n"):
        if char == next_char:
            count += 1
        else:
            encoded += f"{count}{char}"
            count = 1
    return encoded


def decode_run_length(encoded_string):
    """Again, aware this could be much cleaner. In a hurry right now."""
    string = ""
    for x in range(0, len(encoded_string), 2):
        num, char = encoded_string[x], encoded_string[x + 1]
        string += "".join([char] * int(num))
    return string
