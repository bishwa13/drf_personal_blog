import nepali_datetime as nd
import csv

def days_in_nepali_month(year, month):
    # Calculate the number of days in a given Nepali month
    start_date = nd.date(year, month, 1)
    if month == 12:
        next_month = nd.date(year + 1, 1, 1)
    else:
        next_month = nd.date(year, month + 1, 1)
    return (next_month - start_date).days

# Define the range of years for which you want the calendar
start_year = 2080
end_year = 2090
file_name = 'nepali_calendar_2080_2090.csv'

# Open a CSV file to write the calendar data
with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Year', 'Month', 'Day', 'Day of Week', 'Nepali Date'])

    # Iterate over the years
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):  # Nepali months range from 1 to 12
            # Get the number of days in the current Nepali month
            days_in_month = days_in_nepali_month(year, month)
            for day in range(1, days_in_month + 1):
                # Create a Nepali date object
                nepali_date = nd.date(year, month, day)
                # Get the corresponding weekday (0: Sunday, 1: Monday, ..., 6: Saturday)
                day_of_week = nepali_date.strftime('%A')
                # Write the date details to the CSV file
                writer.writerow([year, month, day, day_of_week, nepali_date.strftime('%Y-%m-%d')])

print('Nepali calendar from 2080 to 2090 has been written to', file_name)
