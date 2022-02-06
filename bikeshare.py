import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
            city = input ("welcome: what city number would you like to see its data (chicago,new york city,washington)")
            if city in ['chicago', 'new york city','washington']:
                 break
            else:
                 print("invalid option------notice: be carefull when you type the city name ")
                 continue
             
           
    # TO DO: get user input for month (all, january, february, ... , june)
    month='all'
    day="all"

    filter=input("would you like to filter your data using month or day or both ?")
    if filter == "both"or filter=='month':
        while True:
                month = input("enter the month you want to filter with (january, february, march, april, may, june ,all)").lower()
                if month in ['january', 'february', 'march', 'april', 'may', 'june','all']:                
                    break    
                else:
                    print("invalid entry ")
                    continue
            

     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
   
    if filter == 'both'or filter =="day":
        while True:
            
                day=input("please enter the day you want to filter the data with (sunday, monday, tuesday, wednesday, thursday, friday, saturday all)").lower()
                if day in ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']:              
                    break
                else:
                    print ("please re enter the name of the day")
                    continue
           


    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    data = pd.read_csv(CITY_DATA[city])

    data['Start Time'] = pd.to_datetime(data['Start Time'])

    data['month'] = data['Start Time'].dt.month
    data['day'] = data['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        data = data[data['month'] == month]

    
    if day != 'all':
        data = data[data['day'] == day.title()]    
    

    return data


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month =(df['month']).mode()[0]

    # TO DO: display the most common day of week
    common_day=(df["day"]).mode()[0]

    # TO DO: display the most common start hour
    common_hour=(df["Start Time"].dt.hour).mode()[0]
    print("Mosth common day is "+str(common_day))
    print("Mosth common month is "+str(common_month))
    print("Mosth common hour is "+str(common_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print("the most commonly used start station is {}".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print("the most commonly used end station is {}  ".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station=(df["Start Station"] + "  / " +df['End Station']).mode()[0]
    print("the most frequent combination of start station and end station trip is {}".format(start_end_station))
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_travel=np.sum(df["Trip Duration"])
    print("the total time traveled in hours is  {} ".format(total_time_travel))
    # TO DO: display mean travel time
    mean_travel_time= np.mean(df["Trip Duration"])
    print("the average time traveled in hours  is {} ".format(mean_travel_time ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()

    print(user_types)
    if 'Gender' in df:
    

     # TO DO: Display counts of gender
        user_gender=df["Gender"].value_counts()
        print(user_gender)

     # TO DO: Display earliest, most recent, and most common year of birth
    
        earliest_birth=df['Birth Year'].min()
        print("the earliest year of birth is {} ".format(earliest_birth))
        recent_birth=df["Birth Year"].max()
        print("the recent year of birth is {}".format(recent_birth))
        common_year=df['Birth Year'].mode()[0]
        print("the most common year of birth is {}".format(common_year))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def sample(df):
    print(df.head())
    start_index =5
    while True:
        data_r = input("Would you like to see sample data? (yes/no)")
        if data_r == 'yes':
            temp = pd.DataFrame(df.iloc[start_index:start_index+5])
            print(temp)
            start_index+=5
        else:
            break
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        sample(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
