""" Author  :: Amisha Patel 
    Created :: 03/16/2021
    Assigment ::Testing Mock the GitHub API """
import unittest
from unittest import mock
from amishapatel_hw04 import UserRepos, UserCommit

class TestHW04(unittest.TestCase):
    @mock.patch('amishapatel_hw04.UserRepos')
    def test_UserRepos(self,mockedReq):
        mockedReq.return_value = ['checkbox', 'dot-box-game', 'GITHUB_API_567', 'HW12', 'project', 'SSW-567A', 'SSW555', 'tic-tac-toe', 'TodoList', 'triangle567', 'wp_projects']
        expectresult =['checkbox', 'dot-box-game', 'GITHUB_API_567', 'HW08', 'HW10','HW12', 'project', 'SSW-567A', 'SSW555', 'tic-tac-toe', 'TodoList', 'triangle567', 'wp_projects']
        self.assertNotIn(UserRepos('patelamisha'),expectresult)
        
        
    @mock.patch('amishapatel_hw04.UserCommit')
    def test_UserCommit(self,mockedReq):
        mockedReq.return_value = 2
        self.assertEqual(4, UserCommit('patelamisha', 'checkbox'))
        self.assertNotEqual(8, UserCommit("patelamisha", "TodoList"))
  
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

