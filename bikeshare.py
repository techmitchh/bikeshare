import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_input = False
    month_input = False
    day_input = False
    cities = ['chicago', 'new york', 'washington']
    months = ['all', 'january', 'february', 'mar', 'apr', 'may', 'jun']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'fri', 'sat', 'sun']

    
    while not city_input:
        city = input(f"What city would you like to see data for: {', '.join(cities)}?: ").lower()
        if city not in cities:
            print("Sorry your input was not correct. Please input Chicago, New York, Washington ")
        else:
            city_input = True

    while not month_input:
        month = input(f"Which month would you like to filter by: {', '.join(months)}? ").lower()
        if month not in months:
            print("Sorry your input was not correct. Please input the correct month ")
        else:
            month_input = True

    while not day_input:
        day = input(f"What day would you like data for: {', '.join(days)}? ").lower()
        if day not in days:
            print("Sorry your input was not correct. Please input the correct day")
        else:
            day_input = True

    print('-'*40)
    print(city, month, day)
    
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
    
    # # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    print(df)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
  

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    
    popular_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]

    print(popular_month, popular_day, popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# def station_stats(df):
#     """Displays statistics on the most popular stations and trip."""

#     print('\nCalculating The Most Popular Stations and Trip...\n')
#     start_time = time.time()

#     # TO DO: display most commonly used start station


#     # TO DO: display most commonly used end station


#     # TO DO: display most frequent combination of start station and end station trip


#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


# def trip_duration_stats(df):
#     """Displays statistics on the total and average trip duration."""

#     print('\nCalculating Trip Duration...\n')
#     start_time = time.time()

#     # TO DO: display total travel time


#     # TO DO: display mean travel time


#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


# def user_stats(df):
#     """Displays statistics on bikeshare users."""

#     print('\nCalculating User Stats...\n')
#     start_time = time.time()

#     # TO DO: Display counts of user types


#     # TO DO: Display counts of gender


#     # TO DO: Display earliest, most recent, and most common year of birth


#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        # station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)

        # restart = input('\nWould you like to restart? Enter yes or no.\n')
        # if restart.lower() != 'yes':
        #     break


if __name__ == "__main__":
	main()
