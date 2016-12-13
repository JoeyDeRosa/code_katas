'''Test string_reverse_mirror.py.'''


s1, s2 ="FizZ", "buZZ"
test.assert_equals(reverseAndMirror(s1,s2), "zzUB@@@zZIffIZz")

s1, s2 ="String Reversing", "Changing Case"
test.assert_equals(reverseAndMirror(s1,s2), "ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING")
