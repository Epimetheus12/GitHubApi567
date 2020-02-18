import unittest
from HW04a_Fangji_Liang import get_repo, UrlOpenError

class TestHW04a(unittest.TestCase):

    def test_result(self):
        test_result = ["Repo: GitHubApi567 Number of commits: 9",
         "Repo: SSW-567-HW Number of commits: 1",
         "Repo: SSW-567-HW01-Triangle Number of commits: 2",
         "Repo: Student-Repository Number of commits: 1",
         "Repo: Triangle567 Number of commits: 6"]
        self.assertEqual(get_repo('Epimetheus12'),test_result)
    
    def test_HTTPerror(self):
        with self.assertRaises(UrlOpenError):
            get_repo(['not exist'])

if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)
