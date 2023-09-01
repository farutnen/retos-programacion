import re
import unidecode

def __char_counter(text: str) -> dict[str, int]:
    
    no_number_text = re.sub(r'\d+', '', unidecode(text.lower()))
    no_punt_text = re.sub(r'[\w\s]+', '', no_number_text())
    
    print(no_punt_text)
    
    char_counter = dict()
    
    
    for char in no_punt_text:
        if char in char_counter.keys():
            char_counter[char] += 1
        else:
            char_counter[char] = 1


def isHeterogram(text: str) -> bool:
    for counter in __char_counter(text).values():
        if counter > 1:
            return False
    return True

def isIsogram(text: str) -> bool:
    order = 0
    for counter in __char_counter(text).values():
        if order is 0:
            order = counter
        if order is not counter:
            return False
        
    return True

def isPangram(text: str) -> bool:
    return len(__char_counter(text).keys()) is 27
    