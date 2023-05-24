from plate_validator import PlateValidator
from pico_y_placa_checker import PicoYPlacaChecker

plate_number = input("Enter a plate number: ")
if not PlateValidator.validate_plate_number(plate_number):
    print("Plate number is invalid.")
    exit(1) 

date_string = input("Please enter a date (e.g dd/mm/yyyy hh/mm):")

    
result = PicoYPlacaChecker.can_drive_on(date_string, plate_number)

if result:
    print("The car can drive on the road")
else:
    print("The car cannot drive on the road")
