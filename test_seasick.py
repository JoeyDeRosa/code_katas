'''Test file for seasick_snorkelling.py.'''


Test.describe("Basic tests")
Test.assert_equals(sea_sick("~"), "No Problem")
Test.assert_equals(sea_sick("_~~~~~~~_~__~______~~__~~_~~"), "Throw Up")
Test.assert_equals(sea_sick("______~___~_"), "Throw Up")
Test.assert_equals(sea_sick("____"), "No Problem")
Test.assert_equals(sea_sick("_~~_~____~~~~~~~__~_~"), "Throw Up")