# This file contains the bar codes using in the RM4SCC

class RM4SCC(object):
    symbols = ('S', 'D', 'U', 'L')
    CONTROL_CODES = {
        'S': '<START>',
        'L': '<END>',
    }
    BAR_CODES = {
        'DUDU': 'A',
        'DLSU': 'B',
        'SULD': 'C',
        'SLUD': 'D',
        'SLLS': 'E',
        'DUUD': 'F',
        'DULS': 'G',
        'DLUS': 'H',
        'USDL': 'I',
        'UDSL': 'J',
        'UDDU': 'K',
        'LSSL': 'L',
        'LSDU': 'M',
        'LDSU': 'N',
        'USLD': 'O',
        'UDUD': 'P',
        'UDLS': 'Q',
        'LSUD': 'R',
        'LSLS': 'S',
        'LDUS': 'T',
        'UUDD': 'U',
        'ULSD': 'V',
        'ULDS': 'W',
        'LUSD': 'X',
        'LUDS': 'Y',
        'LLSS': 'Z',
        'SSLL': '0',
        'SDUL': '1',
        'SDLU': '2',
        'DSUL': '3',
        'DSLU': '4',
        'DDUU': '5',
        'SUDL': '6',
        'SLSL': '7',
        'SLDU': '8',
        'DUSL': '9',
    }

