'''test file hw05a, the mock section
Fangji Liang
'''
import unittest
from unittest import mock
from unittest.mock import MagicMock as Mock, patch
from HW04a_Fangji_Liang import get_repo, UrlOpenError
import json



class TestHW04a(unittest.TestCase):
    
    @patch('HW04a_Fangji_Liang.request.urlopen') 
    def test_result(self, mock_urlopen):
        '''Mock the urlopen as a file and read when hw04a call urlopen'''
        mock_urlopen.return_value.read.return_value = bytes('[{"name":"GitHubApi567"}, {"name":"SSW-567-HW"}, \
                                                            {"name":"SSW-567-HW01-Triangle"}, {"name":"Student-Repository"},\
                                                            {"name":"Triangle567"}]', encoding="utf8")

        test_result = ["Repo: GitHubApi567 Number of commits: 5",
         "Repo: SSW-567-HW Number of commits: 5",
         "Repo: SSW-567-HW01-Triangle Number of commits: 5",
         "Repo: Student-Repository Number of commits: 5",
         "Repo: Triangle567 Number of commits: 5"]
        
        self.assertEqual(get_repo('Epimetheus12'), test_result)

    def test_HTTPerror(self):
        with self.assertRaises(UrlOpenError):
            get_repo(['NotExist'])
if __name__ == "__main__":


    unittest.main(exit = False, verbosity = 2)