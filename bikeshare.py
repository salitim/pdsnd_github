import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input("Enter the city name to explore: ")).lower()
        if city in ("chicago", "new york city", "washington"):
            break
        else:
            print("Enter a valid city.")

    # Get user input for month (all, january, february, ... , june)
    while True:
        month = str(
            input("Enter month (for all months enter \"all\"): ")).lower()
        if month in ("all", "january", "february", "march", "april", "may", "june"):
            break
        else:
            print(
                "Enter one of these months :january,february,march,april,may,june or \"all\" for all months.")

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("Enter day name(for all months enter \"all\"): ")).lower()
        if day in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"):
            break
        else:
            print("enter a valid day name or all for all days")
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

    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month: {}\n'.format(most_common_month))

    # Display the most common day of week
    most_common_day_week = df['day_of_week'].mode()[0]
    print('The most common day of week: {}\n'.format(most_common_day_week))

    # Display the most common start hour
    most_common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour: {}\n'.format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    most_common_used_start_station = df['Start Station'].mode()[0]
    print('The most common used start station: {}\n'.format(
        most_common_used_start_station))

    # Display most commonly used end station
    most_common_used_end_station = df['End Station'].mode()[0]
    print('The most common used end station: {}\n'.format(
        most_common_used_end_station))

    # Display most frequent combination of start station and end station trip
    most_frequent_star_end_station = df.groupby(
        ['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip: \n{}'.format(
        most_frequent_star_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = datetime.timedelta(
        seconds=int(df['Trip Duration'].sum()))
    print('Total travel time: {}\n'.format(total_travel_time))

    # Display mean travel time
    mean_travel_time = datetime.timedelta(
        seconds=int(df['Trip Duration'].mean()))
    print('Mean travel time: {}\n'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print('Number of user types : {}\n'.format(user_types_counts))

    # Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('Number of gender types: {}\n'.format(gender_counts))
    except:
        print('No gender data for this city\n')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year_birth = df['Birth Year'].min()
        later_year_birth = df['Birth Year'].max()
        common_year_birth = df['Birth Year'].mode()[0]
        print('Earliest year of birth: {}\n'.format(earliest_year_birth))
        print('Later year of birth: {}\n'.format(later_year_birth))
        print('Common year of birth: {}\n'.format(common_year_birth))
    except:
        print('No birthday data for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
