import unittest
import Parser
import filecmp


class TestStringMethods(unittest.TestCase):

    def test_main(self):
        Parser.main("test1.gjf", "", "")
        results = filecmp.cmp('test1_mod.gjf', 'test1_expected.gjf')
        self.assertTrue(results, "test1 crashed")

    def water_test(self):
        Parser.main("water.gjf", "", "")
        results = filecmp.cmp('water_mod.gjf', 'water_expected.gjf')
        self.assertTrue(results, "water crashed")

    def test_space(self):
        Parser.main("testspace.gjf", "", "")
        results = filecmp.cmp('testspace_mod.gjf', 'testspace_expected.gjf')
        self.assertTrue(results, "testspace crashed")

if __name__ == '__main__':
    unittest.main()