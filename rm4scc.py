# This file contains the bar codes used in the RM4SCC
import numpy as np


class RM4SCC(object):

    # base symbols
    symbols = (
        'S',  # Short
        'D',  # Descender
        'A',  # Ascender
        'L'   # Long
    )

    # symbol representation
    symbol_bars = (
        ('0', '0'),  # Short
        ('0', '1'),  # Descender
        ('1', '0'),  # Ascender
        ('1', '1'),  # Long
    )

    # control characters
    START = 'A'
    END = 'L'

    # all codes
    BAR_CODES = {
        'DADA': 'A',
        'DLSA': 'B',
        'SALD': 'C',
        'SLAD': 'D',
        'SLLS': 'E',
        'DAAD': 'F',
        'DALS': 'G',
        'DLAS': 'H',
        'ASDL': 'I',
        'ADSL': 'J',
        'ADDA': 'K',
        'LSSL': 'L',
        'LSDA': 'M',
        'LDSA': 'N',
        'ASLD': 'O',
        'ADAD': 'P',
        'ADLS': 'Q',
        'LSAD': 'R',
        'LSLS': 'S',
        'LDAS': 'T',
        'AADD': 'A',
        'ALSD': 'V',
        'ALDS': 'W',
        'LASD': 'X',
        'LADS': 'Y',
        'LLSS': 'Z',
        'SSLL': '0',
        'SDAL': '1',
        'SDLA': '2',
        'DSAL': '3',
        'DSLA': '4',
        'DDAA': '5',
        'SADL': '6',
        'SLSL': '7',
        'SLDA': '8',
        'DASL': '9',
    }

    @staticmethod
    def checksum(codeword):
        """Compute the checksum for the codeword specified.
        The last code of the codeword is considered to be the checksum to check against and it is skipped."""
        upper = 0
        lower = 0
        weights = np.array([4, 2, 1, 0])

        for code in codeword[:-1]:
            symbol = [k for k, v in RM4SCC.BAR_CODES.items() if v == code][0]
            upper += (np.array([1 if c in ('A', 'L') else 0 for c in symbol]) * weights).sum()
            lower += (np.array([1 if c in ('D', 'L') else 0 for c in symbol]) * weights).sum()

        half_sums = []
        for hsum in [upper, lower]:
            hsum %= 6
            hsum = 6 if hsum == 0 else hsum

            binary = '{:03b}'.format(hsum)
            # Ensure even-parity in terms of ascenders/descenders
            if binary.count('1') == 1:
                binary += '1'
            else:
                binary += '0'
            half_sums.append(binary)

        checksum_char = ''.join([RM4SCC.symbols[RM4SCC.symbol_bars.index(t)] for t in zip(*half_sums)])
        return RM4SCC.BAR_CODES[checksum_char]

    @staticmethod
    def decodeSymbols(symbols):
        """Given a list of symbols, including start and stop characters, return the decoded codeword

        :param symbols: list of characters in RM4SCC.symbols
        :return: codeword as a string

        """
        assert len(symbols) > 2 and len(symbols) % 4 == 0, 'Invalid length'
        assert symbols.pop(0) == RM4SCC.START, 'No "START" symbol'
        assert symbols.pop(-1) == RM4SCC.END, 'No "END" symbol'

        # Group symbols 4 by 4
        codes = zip(*[symbols[i::4] for i in range(4)])
        codeword = [RM4SCC.BAR_CODES[''.join(code)] for code in codes]

        checksum = RM4SCC.checksum(codeword)
        assert codeword[-1] == checksum, 'Checksum failed. Is: {}. Should be: {}.'.\
            format(codeword[-1], checksum)

        return ''.join(codeword)
