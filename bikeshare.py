import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ["monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday", "sunday", "all"]

# get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    print("Please, Answer question")
    city = input("Would you like to see data for Chicago, New York City, or Washington ? ").lower()
    while city not in cities:
        print("wrong input\nTry Again")
        city = input("Would you like to see data for Chicago, New York City, or Washington ? ").lower()

    while city in cities:
        print(f"Your city is : {city}")
        TimeFrame = input("Would you like to filter the data by month, day, or together ? ").lower()
        
    # get user input for month (all, january, february, ... , june)
    
        if TimeFrame == "month":
            month = input("Which month - January, February, March, April, May, or June ? ").lower()
            while month not in months:
                print("wrong input\nTry Again")
                month = input("Which month - January, February, March, April, May, or June ? ").lower() 
            else:
                day = "all"
                print(f"your month choice is {month}")
                break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
        elif TimeFrame == "day":
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday ? ").lower()
            while day not in days:
                print("wrong input\nTry Again")
                day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday ? ").lower()
            else:
                month = "all"
                print(f"your day choice is {day}")
                break
    #get user input for month and day of week (together)
    
        elif TimeFrame == "together":
            month = input("Which month - January, February, March, April, May, or June ? ").lower()
            while month not in months:
                print("wrong input\nTry Again")
                month = input("Which month - January, February, March, April, May, or June ? ").lower() 
            else:
                day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday ? ").lower()
                while day not in days:
                     print("wrong input\nTry Again")
                     day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday ? ").lower()
                else:
                     print(f"Your month choice is {month}\nYour day choice is {day}")
                     break
        else:
            print("wrong input\nTry Again")
            TimeFrame = input("Would you like to filter the data by month, day, or together ? ").lower()
    
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
    

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
         # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
         df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f'Most common month:{common_month}')
       

    # TO DO: display the most common day of week
    common_dayofweek = df['day_of_week'].mode()[0]
    print(f'Most common day of week:{common_dayofweek}')

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print(f'Most common start hour: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_startstation = df["Start Station"].mode()[0]
    print(f'Most common start station: {common_startstation}')

    # TO DO: display most commonly used end station
    common_endstation = df["End Station"].mode()[0]
    print(f'Most common start station: {common_endstation}')

    # TO DO: display most frequent combination of start station and end station trip
    df["combination_start_end"] = df["Start Station"] + df["End Station"]
    common_combination_start_end = df["combination_start_end"].mode()[0]
    print(f'Most common trip from start to end : {common_combination_start_end}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = df['Trip Duration'].sum()
    print(f'total travel time : {tot_travel_time}')

    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print(f'Average travel time : {mean_travel_time}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df["User Type"].value_counts()
    print(f'Count of each user type : {user_type}')

    # TO DO: Display counts of gender
    try:
        count_gender = df["Gender"].value_counts()
        print(f'Count of Gender : {count_gender}')
    except:
        print("gender column doesn't exist")
    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
       min_year = df["Birth Year"].min()
       max_year = df["Birth Year"].max()
       common_year = df["Birth Year"].mode()[0]
       print(f'Earliest year : {min_year}\nMost recent year : {max_year}\nMost common year of birth : {min_year}')
    except:
        print("gender column doesn't exist") 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    display_raw = input('\n Would you like to see the raw data? Enter yes or no.\n')
    while display_raw == 'yes':
         try:
             for chunk in pd.read_csv(CITY_DATA[city],chunksize=5):
                 print(chunk)
                 display_raw = input('\nWould you like to see another 5 rows of the raw data? Enter yes or no.\n')
                 if display_raw != 'yes':
                     print('Thank You')
                     break #breaking out of the for loop
             break
         except KeyboardInterrupt:
               print('Thank you.')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
