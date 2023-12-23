import re
from pathlib import Path

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")
TRANS = {}

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic)] = latin
    TRANS[ord(cyrillic.upper())] = latin.upper()


def normalize(name: str) -> str:
    translate_word = str(re.sub(r'\W', '_', name.translate(TRANS)))
    # first version
    translate_word = change_name(translate_word)

    # second version
    # translate_word = re.sub(r'_'+Path(name).suffix[1:], '.'+Path(name).suffix[1:], translate_word) 
    
    return translate_word

def change_name(translate_word):
    index_str = translate_word.rfind('_')
    result = translate_word.replace(translate_word[index_str:], '.'+translate_word[index_str+1:])
    return result