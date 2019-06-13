import re
def kontti(s):
    return re.sub('(?i)(\S*?[aeiouy])(\S*)', r'ko\2-\1ntti', s, flags = re.I)