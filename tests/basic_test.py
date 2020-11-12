import unittest
import Parser
import filecmp


class TestStringMethods(unittest.TestCase):

  def test_main(self):
      Parser.main("test1.gjf", "", "")
      results = filecmp.cmp('test1_mod.gjf', 'test1_expected.gjf')
      self.assertTrue(results)


if __name__ == '__main__':
    unittest.main()