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

    def test_firstlast(self):
        self.e_list = ["Kobe", 2, 24, 8, "Gigi"]
        self.firstlast = task.firstlast(self.e_list)
        self.test_list = ["Kobe", "Gigi"]
        self.assertListEqual(self.firstlast, self.test_list)

    def test_date(self):
        self.days_between = task.daysbetween(2019, 1, 23, 2020, 1, 23)
        self.assertEqual(365, self.days_between)


if __name__ == '__main__':
    unittest.main()
