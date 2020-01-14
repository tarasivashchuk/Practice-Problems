"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
"""

from practice_problems.solutions.run_length_encoding import decode_run_length, \
    encode_run_length

encoded_example = ("AAAABBBCCDAA", "4A3B2C1D2A")


def test_encode_run_length():
    encoded = encode_run_length(encoded_example[0])
    assert encoded == encoded_example[1]


def test_decode_run_length():
    decoded = decode_run_length(encoded_example[1])
    assert decoded == encoded_example[0]
