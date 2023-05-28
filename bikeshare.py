import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    random changes

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("Which city do you want to analyze between Washington, New York City, and Chicago?\n").lower().strip()
      if city not in ('new york city', 'chicago', 'washington'):
        print("Try again between Washington, New York City or Chicago.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("Which month would you like to analyze between January, February, March, April, May, June or all?\n").lower().strip()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Try again between January, February, March, April, May, June or all.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("Which day of week would you like to analyze between Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all'\n").lower().strip()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("Sorry, I didn't catch that. Try again.")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day is: ", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("The most common hour is: ", df['Start Time'].dt.hour.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most common end station is: ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip\n", df.groupby(['Start Station', 'End Station']).size().nlargest(1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time:', sum(df['Trip Duration'])/86400, " Days")

    # TO DO: display mean travel time
    print('Mean travel time:', df['Trip Duration'].mean()/3600, " Hours")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
      print('Counts of user types:\n', df['User Type'].value_counts())
    except KeyError:
      print("No data available.")
    
    # TO DO: Display counts of gender
    try:
      print('Counts of gender:\n', df['Gender'].value_counts())
    except KeyError:
      print("No data available.")
    


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      print('\nEarliest Year:', int(df['Birth Year'].min()))
    except KeyError:
      print("No data available.")

    try:
      print('\nMost Recent Year:', int(df['Birth Year'].max()))
    except KeyError:
      print("No data available.")

    try:
      print('\nMost Common Year:', int(df['Birth Year'].value_counts().idxmax()))
    except KeyError:
      print("No data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower().strip()
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower().strip()
        if view_data.lower().strip() != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
