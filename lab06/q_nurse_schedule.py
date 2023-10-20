#!/usr/bin/env python3

import datetime

def patient_schedule(patient_name, interval_in_hours):
    """
    This function will take a patient name and corresponding medication
    interval and return a list of tuples where each tuple contains the
    patient name and medication time in datetime object format.
    """
    # Get the current datetime
    now = datetime.datetime.now()

    # Calculate the end date (14 days from now)
    end_date = now + datetime.timedelta(days=14)

    # Initialize the schedule list
    schedule = []

    # Initialize the next medication time
    next_medication_time = now

    while next_medication_time <= end_date:
        # Add the medication time to the schedule
        schedule.append((patient_name, next_medication_time))

        # Calculate the next medication time
        next_medication_time += datetime.timedelta(hours=interval_in_hours)

    return schedule

def main():
    """
    Florence is a nurse in a clinic. She is caring for 4 patients on
    different medication schedules.

    * Mark needs medication every 5 hours
    * Susan needs medication every 3 hours
    * Chloe needs medication every 8 hours
    * Alexander needs medication every 10 hours
    """

    # Get the medication schedules for each patient
    mark_schedule = patient_schedule("Mark", 5)
    susan_schedule = patient_schedule("Susan", 3)
    chloe_schedule = patient_schedule("Chloe", 8)
    alexander_schedule = patient_schedule("Alexander", 10)

    # Combine all the schedules into one list
    combined_schedule = mark_schedule + susan_schedule + chloe_schedule + alexander_schedule

    # Sort the combined schedule by time
    combined_schedule.sort(key=lambda x: x[1])

    # Print the medication schedule
    for patient_name, medication_time in combined_schedule:
        print(medication_time.strftime("%A, %d %m %Y, %H:%M:%S"), "Time to give medication to", patient_name)

if __name__ == "__main__":
    main()
