import unittest

from Tower import Tower


class TowerTest(unittest.TestCase):
    def test_set_image(self):
        tower = Tower()
        tower.set_image()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
