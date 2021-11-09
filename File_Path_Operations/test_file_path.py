'''Test file for file_path_operations.py.'''


master = FileMaster('/Users/person1/Pictures/house.png')
test.describe('Description Test Cases')
test.assert_equals(master.extension(), 'png')
test.assert_equals(master.filename(), 'house')
test.assert_equals(master.dirpath(), '/Users/person1/Pictures/')