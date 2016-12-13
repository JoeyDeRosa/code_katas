'''Test for sum_of_nth_terms.py.'''
test_list = [
    [0, '0.00'],
    [1, '1.00'],
    [2, '1.25'],
    [3, '1.39'],
]


def test_series_sum():
    '''Test that series_sum returns the correct answer from the table.'''
    from sum_of_nth_terms.py import series_sum
    for i in test_list:
        assert series_sum(i[0]) == i[1]
