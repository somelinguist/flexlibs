import unittest
from flexlibs import FLExInit
from flexlibs.FLExDBAccess import FLExProject


class TestFLExProject(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        FLExInit.Initialize()
        cls.project = FLExProject()

    @classmethod
    def tearDownClass(cls):
        FLExInit.Cleanup()

    def test_GetProjectNames(self):
        self.assertIsInstance(self.project.GetProjectNames(), list)

    def test_OpenProject(self):
        pass


if __name__ == "__main__":
    unittest.main()
