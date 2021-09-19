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
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    
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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])     # convert the Start Time column to datetime
    
    df['month'] = df['Start Time'].dt.month                 # extract month and day of week from Start Time to create new columns
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
   
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']         # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
    
        df = df[df['month'] == month]        # filter by month to create the new dataframe

        

    if day != 'all':    # filter by day of week if applicable
        days = ['monday','tuesday','wednesday','Thursday','friday','saturday','sunday']
        day = days.index(day)
        df = df[df['day_of_week'] == day]        # filter by day of week to create the new dataframe
        
    return df

def time_stats(df): 
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    print(df)
    # TO DO: display the most common month
    com_month = df['month'].mode()
    print(com_month)
    # TO DO: display the most common day of week
    com_day = df['day_of_week'].mode()
    # TO DO: display the most common start hour
    com_hour = df['hour'].mode()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    common_ststation = df['Start Station'].value_counts()
    print("The top 5 common Start Station's are...\n{}\n\n".format(common_ststation.head(1)))
    # TO DO: display most commonly used end station
    common_enstation = df['End Station'].value_counts()
    print("The top 5 common End Station's are...\n{}\n\n".format(common_enstation.head(1)))
    # TO DO: display most frequent combination of start station and end station trip
    start_endstation = df.groupby(['Start Station'])['End Station'].value_counts()
    print(start_endstation.head(1))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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

        # time_stats(df)
        station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)

        # restart = input('\nWould you like to restart? Enter yes or no.\n')
        # if restart.lower() != 'yes':
        #     break


if __name__ == "__main__":
	main()
