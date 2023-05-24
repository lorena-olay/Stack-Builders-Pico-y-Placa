import unittest
from main import check_if_can_drive

class TestMain(unittest.TestCase):
    def test_check_if_can_drive(self):
        self.assertEqual(check_if_can_drive('20/05/2023 10:00', 'ABC-1234'), 'The car can drive on the road.')
        self.assertEqual(check_if_can_drive('22/05/2023 10:00', 'ABC-1235'), 'The car cannot drive on the road.')
        self.assertEqual(check_if_can_drive('22/05/2023 10:00', '123-ABC'), 'Plate number is invalid.')

if __name__ == "__main__":
    unittest.main()
