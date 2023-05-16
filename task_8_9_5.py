from utils import print_intro

print_intro()

MONTH_DAYS = {'january': '31',
              'february': '28 or 29',
              'march': '31',
              'april': '30',
              'may': '31',
              'june': '30',
              'july': '31',
              'august': '31',
              'september': '30',
              'october': '31',
              'november': '30',
              'december': '31'}


def print_days_in_month(month, days_in_month):
    # Check if the correct month name has been entered
    massage = f'Number of days in {month}: {days_in_month}' if days_in_month is not None \
        else 'Invalid month name.'
    print(massage)


if __name__ == '__main__':
    month_name = input('Enter month name: ')
    days = MONTH_DAYS.get(month_name.lower())  # Get the number of days in a month
    print_days_in_month(month_name, days)
