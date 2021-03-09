""" Author  :: Amisha Patel 
    Created :: 03/08/2021
    Assigment ::Testing GIT Repositories & Commits """
import unittest
from amishapatel_hw04 import UserRepos, UserCommit

class TestHW04(unittest.TestCase):
    
    def test_UserRepos(self):
        self.assertIn("HW08", UserRepos("patelamisha"))
        self.assertNotIn("SSW", UserRepos("patelamisha"))
        self.assertIn("triangle567", UserRepos("patelamisha"))
        self.assertNotIn("HW", UserRepos("patelamisha"))
    def test_UserCommit(self):
        self.assertEqual(4, UserCommit("patelamisha", "checkbox"))
        self.assertNotEqual(8, UserCommit("patelamisha", "TodoList"))
        self.assertEqual(8, UserCommit("patelamisha", "triangle567"))
        self.assertNotEqual(2, UserCommit("patelamisha", "SSW-567A"))
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()