from rm4scc import RM4SCC
from nose.tools import assert_raises, assert_equal


class TestRM4SCC(object):
    def test_decode_symbols_empty_list_of_symbols(self):
        assert_raises(AssertionError, RM4SCC.decodeSymbols, [''])

    def test_decode_symbols_no_start(self):
        assert_raises(AssertionError, RM4SCC.decodeSymbols, ['L'])

    def test_decode_symbols_no_end(self):
        assert_raises(AssertionError, RM4SCC.decodeSymbols, ['A'])

    def test_decode_symbols_start_and_end_only(self):
        assert_raises(AssertionError, RM4SCC.decodeSymbols, ['A', 'L'])

    def test_decode_symbols_no_checksum(self):
        assert_raises(AssertionError, RM4SCC.decodeSymbols, [c for c in 'ADALSL'])

    def test_decode_symbols_not_multiple_of_4(self):
        assert_raises(AssertionError, RM4SCC.decodeSymbols, [c for c in 'ADASL'])

    def test_decode_symbols_valid_single_char(self):
        ret = RM4SCC.decodeSymbols([c for c in 'ADASLDASLL'])
        assert_equal(ret, '99')

    def test_decode_symbols_valid_multiple_chars(self):
        ret = RM4SCC.decodeSymbols([c for c in 'ADASLSLSLLSADADDAADADALDSL'])
        assert_equal(ret, '97RKPW')
