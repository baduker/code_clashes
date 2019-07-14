import re


def pete_talk(speech, ok=[]):
    just_words = r"\b((\w)(\w*)(\w))\b"
    punctuation = r"((^|[.!?])\s*)(\w)"
    
    ok = [word.lower() for word in ok]
    
    def mask(match):
        if match.group() not in ok:
            return match.group(2) + "*" * len(match.group(3)) + match.group(4)
        else:
            return match.group()
    
    
    def cap(match):
        return match.group(1) + match.group(3).title()
    
    
    speech = re.sub(just_words, mask, speech.lower())
    speech = re.sub(punctuation, cap, speech)
    
    return speech