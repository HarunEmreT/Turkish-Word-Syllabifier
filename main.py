# -*- coding: utf-8 -*-
# Copyright (c) 2026 Harun Emre Tutal
# Licensed under the MIT License
# -*- author: Harun Emre Tutal -*-
# -*- title: Türkçe Kelime Heceleme / Turkish Word Syllabifier -*-
# -*- version: v0.0.0 -*-

from sys import argv
from _syllabifier import _Syllabifier, ForeignLetterException


def main():
    """ This function starts the program
    """
    word = argv[1]
    try:
        syllables = _Syllabifier.syllabify(word)
        print("\nHeceler : ", end="")
        print(*syllables, sep=" / ")
    except ForeignLetterException:
        print("Bu kelime yabancı bir harf içeriyor.")


if __name__ == "__main__":
    main()
