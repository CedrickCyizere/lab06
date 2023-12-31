#!/usr/bin/env python3

import datetime



def main():
    """
    Create a datetime object for today's date
    """
    todays_date = datetime.date.today()

    date_list = every_lab(todays_date)

    """ 
    variable date_list should contain datetime objects 
    for all the days when you have a lab
    print these dates in the format "Mon, 19 November 23"
    """
    for date in date_list:
        print(date.strftime("%a, %d %B %y"))


def every_lab(todays_date):
    """
    Classes for the current semester end on Dec 4, 2023.

    Assume that you have a lab every week till the end of classes. 
    (Only your lab, in this instance.)

    This function will create datetimes objects for those labs, 
    add them to a list and then return this list
    """
    end_date = datetime.date(2023, 12, 4)
    one_week = datetime.timedelta(days=7)

    lab_dates = []
    
    next_lab_date = todays_date
    while next_lab_date <= end_date:
        lab_dates.append(next_lab_date)
        next_lab_date += one_week

    return lab_dates

if __name__ == "__main__":
    main()
