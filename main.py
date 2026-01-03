# -*- coding: utf-8 -*-
# -*- author: Harun Emre Tutal -*-
# -*- title: Türkçe Kelime Heceleme / Turkish Word Syllabifier -*-
# -*- version: v0.0.0 -*-

from sys import argv
from _syllabifier import _Syllabifier


def main():
    word = argv[1]
    syllables = _Syllabifier.syllabify(word)
    print("\nSyllables : ", end="")
    print(*syllables, sep=" / ")


if __name__ == "__main__":
    main()
