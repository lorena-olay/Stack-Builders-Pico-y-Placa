import unittest
from plate_validator import PlateValidator

class TestPlateValidator(unittest.TestCase):
    def test_validate_plate_number(self):
        # Test valid plate numbers
        self.assertTrue(PlateValidator.validate_plate_number('ABC-1234'))
        self.assertTrue(PlateValidator.validate_plate_number('XYZ-123'))

        # Test invalid plate numbers
        self.assertFalse(PlateValidator.validate_plate_number('123-ABC'))
        self.assertFalse(PlateValidator.validate_plate_number('ABCD-1234'))
        self.assertFalse(PlateValidator.validate_plate_number('ABC1234'))
        self.assertFalse(PlateValidator.validate_plate_number('ABC-12'))

if __name__ == "__main__":
    unittest.main()
