# -*- coding: utf-8 -*-
# -*- author: Harun Emre Tutal -*-
"""
    Syllabifier static class is contain here
"""

class _Syllabifier:
    """ This class contains functions about slicing Turkish words syllable by syllable.
    """

    VOWELS_TR = "aeıioöuü"
    CONSONANTS_TR = "bcçdfgğhjklmnprsştvyz"

    @classmethod
    def syllabify(cls: "_Syllabifier", word: str) -> list:
        """ This method slices the Turkish words syllable by syllable
        """
        syllables = []
        syllable = ""
        for l in reversed(word):
            lower_l = cls.turkish_lower(l)
            if lower_l not in cls.VOWELS_TR + cls.CONSONANTS_TR:
                raise ForeignLetterException("The word contains a foreign letter in Turkish.")

            if len(syllable) > 0 and syllable[0].lower() in cls.VOWELS_TR:
                if lower_l in cls.CONSONANTS_TR:
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
    def turkish_lower(cls: "_Syllabifier", letter: str) -> str:
        """ This method solves the problem of changing the letter "İ" from uppercase to lowercase.
        """
        if letter == "İ":
            return "i"
        return letter.lower()


class ForeignLetterException(ValueError):
    """ This exception type is for foreign letters """


if __name__ == "__main__":
    print(_Syllabifier.syllabify("Herhangi"))
