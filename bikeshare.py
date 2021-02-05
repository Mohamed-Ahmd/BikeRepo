import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def check_input(input_str,input_type):
    while True:
        input_read=input(input_str)
        try:
            if input_read in ['chicago','new york city','washington'] and input_type==1:
                break
            elif input_read in ['january', 'february', 'march', 'april', 'may', 'june', 'all'] and input_type==2:
                break
            elif input_read in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'] and input_type==3:
                break
            else:
                if input_type==1:
                    print('worng input please type one of the default cities')
                if input_type==2:
                    print('worng input please type one month of the year')
                if input_type==3:
                    print('worng input please type one day of the week')
        except ValueError:
            print('Error Input')
    return input_read

def get_filters():
    city=input('would you input chicago, new york or washington',1)
    month=input('which month of the year',2)
    day=input('which day of the week',3)
    print('_'*40)
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
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    #convert the Start Time column to datrtime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        #use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #filter by month to create the new dateframe
        df = df[df['month'] == month] 

    # filter by day of week if applicale
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df 

def time_stat(df):
    start_time =time.time()
    print(df['month'].mode()[0])
    print(df['day_of_week'].mode()[0])
    print(df['hour'].mode()[0])
    print('Elapsed Time %s seconds', (time.time()-start_time))

def station_stat(df):
    start_time =time.time()
    print(df['Start Starion'].mode()[0])
    print(df['End Station'].mode()[0])
    group_field= df.groupby(['Start Station','End Station'])
    print(group_field.size().sort_values(ascending=False).head(1))
    print('Elapsed Time %s seconds', (time.time()-start_time))

def trip_stat(df):
    print('\ntrip...\n')
    start_time = time.time()
    print(df['Trip Duration'].sum())
    print(df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_' * 40)

def user_stat(df):
    print('\nuser...\n')
    start_time = time.time()
    print(df['User Type'].value_counts())
    if city !='washington':
        print(df['Gender'].value_counts())
        print(df['Birth Year'].mode()[0])
        print(df['Birth Year'].max())
        print(df['Birth Year'].min())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_ ' * 40)

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
start_loc = 0
while True:
    print(df.iloc[0:5])
    start_loc += 5
    view_display = input('\nDo you wish to continue? Enter yes or no\n')
    if view_display !='yes':
        break
        
def main():
    while True:
        city, month, day =get_filters()
        df = load_data( city, month, day)
        
        time_stat(df)
        station_stat(df)
        trip_stat(df)
        user_stat(df,city)
        
        print(df.head())
        
         restart = input('\nWould you like to restart? Enter yes or no\n')
        if restart !='yes':
            break
   


if __name__ ==" __main__ ":
   main()
