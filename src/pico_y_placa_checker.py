from datetime import datetime

class PicoYPlacaChecker:
    @staticmethod
    def can_drive_on(date, plate_number):
        # parse date
        try:
            date = datetime.strptime(date, '%d/%m/%Y %H:%M')
        
            # get last digit of plate number
            last_digit = int(str(plate_number)[-1])

            # check weekday and restrictions
            weekday = date.weekday() # 0 is Monday, 1 is Tuesday, etc.

            if weekday == 0: # Monday
                return last_digit not in [5, 6, 7, 8]
            elif weekday == 1: # Tuesday
                return last_digit not in [9, 0, 1, 2]
            elif weekday == 2: # Wednesday
                return last_digit not in [3, 4, 5, 6]
            elif weekday == 3: # Thursday
                return last_digit not in [7, 8, 9, 0]
            elif weekday == 4: # Friday
                return last_digit not in [1, 2, 3, 4]
            else: # weekend
                return True
            
        except:
            print("An exception occurred")
            exit(1)
            