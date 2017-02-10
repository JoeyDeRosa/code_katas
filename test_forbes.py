"""Test file for forbes."""


def test_forbes():
    """given the forbes list return the expected people."""
    from forbes import forbes
    assert forbes() == ('youngest:', u'Mark Zuckerberg', 44600000000, u'Facebook', 'oldest under 80', u'Phil Knight', 24400000000, u'Nike')
 