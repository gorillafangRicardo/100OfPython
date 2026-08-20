is_leap = True

while is_leap == True:

    def is_leap_year(year):

        if  year % 4 == 0:
            return year
        else:
            return False

    new_value = is_leap_year(year = 2100)
    is_leap = is_leap_year(new_value)

    def divided_100(year):
        if year % 100 == 0:
            return year 
        else:
            return False

        
    last_condition = divided_100(year = new_value)
    is_leap = divided_100(year=new_value)

    def clean_400(year):
        if year % 400 == 0:
            print("Leap year")
        else:
            return False

    clean_400(year = last_condition)
    is_leap = clean_400(year=last_condition)
