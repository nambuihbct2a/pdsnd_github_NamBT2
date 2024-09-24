import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAY_LIST = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

#Funcion get filters for user
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ''
    while city not in CITY_DATA:
        city = input("\nChoose a city (chicago, new york city, washington): ").lower()
    
    month = ''
    while month not in MONTH_DATA:
        month = input("\nChoose a month (january, february, ... , june, all): ").lower()
    
    day = ''
    while day not in DAY_LIST:
        day = input("\nChoose a day (monday, tuesday, ... , sunday, all): ").lower()

    print('-'*80)
    return city, month, day
"""Load data 
    """
def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        month_index = MONTH_DATA.index(month) + 1
        df = df[df['month'] == month_index]

    if day != 'all':
        df = df[df['day_of_week'] == day]
    
    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(f"Most Popular Month: {df['month'].mode()[0]}")
    print(f"Most Popular Day: {df['day_of_week'].mode()[0]}")
    df['hour'] = df['Start Time'].dt.hour
    print(f"Most Popular Start Hour: {df['hour'].mode()[0]}")
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print(f"Most Common Start Station: {df['Start Station'].mode()[0]}")
    print(f"Most Common End Station: {df['End Station'].mode()[0]}")
    df['Start To End'] = df['Start Station'] + " to " + df['End Station']
    print(f"Most Common Trip: {df['Start To End'].mode()[0]}")
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print(f"Total Duration: {hour} hours, {minute} minutes, {second} seconds")
    average_duration = df['Trip Duration'].mean()
    mins, sec = divmod(average_duration, 60)
    print(f"Average Duration: {mins} minutes, {sec} seconds")
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)
"""user_stats 
    """
def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print(f"User Types:\n{df['User Type'].value_counts()}")
    try:
        print(f"\nGender:\n{df['Gender'].value_counts()}")
    except KeyError:
        print("\nNo Gender data available.")
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nBirth Year:\nEarliest: {earliest}\nMost Recent: {recent}\nMost Common: {common_year}")
    except KeyError:
        print("\nNo Birth Year data available.")
    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*80)
"""Display data 
    """
def display_data(df):
    start_loc = 0
    while True:
        display = input("\nDo you want to see 5 rows of raw data? Enter yes or no.\n").lower()
        if display != 'yes':
            break
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
	display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
