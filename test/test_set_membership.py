import unittest
from more_fun_with_collections.set_membership import in_set

class FunctionTests(unittest.TestCase):

    def test_in_set_true(self):
        a_set = {2, 4, 5, 7, 8, 56}
        self.assertTrue(in_set(4, a_set))

    def test_in_set_false(self):
        a_set = {1, 5, 8, 57, 3}
        self.assertFalse(in_set(4, a_set))
