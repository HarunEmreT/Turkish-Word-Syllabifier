# -*- coding: utf-8 -*-
# -*- author: Harun Emre Tutal -*-

class _Syllabifier:
    """ This class slicing the Turkish words syllable by syllable.
    """

    vowels_tr = "aeıioöuü"
    consonants_tr = "bcçdfgğhjklmnprsştvyz"

    @classmethod
    def syllabify(cls, word):
        syllables = []
        syllable = ""
        for l in reversed(word):
            lower_l = cls.turkish_lower(l)
            if lower_l not in cls.vowels_tr + cls.consonants_tr:
                raise ValueError("The word contains a letter that is not Turkish.")

            if len(syllable) > 0 and syllable[0].lower() in cls.vowels_tr:
                if lower_l in cls.consonants_tr:
                    syllable = l + syllable
                    syllables.append(syllable)
                    syllable = ""
                else:
                    syllables.append(syllable)
                    syllable = l
                continue
            syllable = l + syllable

        if syllable:
            syllables.append(syllable)
        return syllables[::-1]

    @classmethod
    def turkish_lower(cls, letter):
        if letter == "İ":
            return "i"
        return letter.lower()


if __name__ == "__main__":
    print(_Syllabifier.syllabify("İrem"))
