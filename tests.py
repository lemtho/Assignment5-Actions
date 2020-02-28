import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_circle(self):
        self.area = task.circle(5)
        self.assertEqual(78.54, self.area)


if __name__ == '__main__':
    unittest.main()
