import unittest
from pico_y_placa_checker import PicoYPlacaChecker

class TestPicoYPlacaChecker(unittest.TestCase):
    def test_can_drive_on(self):
        # Test unrestricted cases
        self.assertTrue(PicoYPlacaChecker.can_drive_on('20/05/2023 10:00', 'ABC-1234'))  # Saturday
        self.assertTrue(PicoYPlacaChecker.can_drive_on('21/05/2023 10:00', 'ABC-1234'))  # Sunday
        self.assertTrue(PicoYPlacaChecker.can_drive_on('22/05/2023 10:00', 'ABC-1234'))  # Monday
        self.assertTrue(PicoYPlacaChecker.can_drive_on('23/05/2023 10:00', 'ABC-1237'))  # Tuesday

        # Test restricted cases
        self.assertFalse(PicoYPlacaChecker.can_drive_on('22/05/2023 10:00', 'ABC-1235'))  # Monday
        self.assertFalse(PicoYPlacaChecker.can_drive_on('23/05/2023 10:00', 'ABC-1239'))  # Tuesday
        self.assertFalse(PicoYPlacaChecker.can_drive_on('24/05/2023 10:00', 'ABC-1236'))  # Wednesday
        self.assertFalse(PicoYPlacaChecker.can_drive_on('25/05/2023 10:00', 'ABC-1239'))  # Thursday
        self.assertFalse(PicoYPlacaChecker.can_drive_on('26/05/2023 10:00', 'ABC-1233'))  # Friday

if __name__ == "__main__":
    unittest.main()
