import re

class PlateValidator:
    @staticmethod
    def validate_plate_number(plate_number):
        # Define the pattern for the plate number format
        pattern = r'^[A-Z]{3}-\d{3,4}$'

        # Check if the plate number matches the pattern
        if re.match(pattern, plate_number):
            return True
        else:
            return False
