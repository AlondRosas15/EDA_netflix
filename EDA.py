import pandas as pd
import random

#dataset came from Kaggle
#https://www.kaggle.com/datasets/shivamb/netflix-shows/data

#read the data
data = pd.read_csv('netflix_titles.csv')

#testing to see if read successfully
#print(data)
#clean it up, see what we can find such as any null present

#what's the shape of the data we are dealing
#print(data.shape)     
#shape is (8807 rows, 12 columns)

#what info are we getting(the columns)

# Set pandas display options to show all columns, seems that I exceeded the default limit
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
#print(data.info())
#our columns are show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, and description
#we have some null present in director, cast, country, date_added,rating,and duration


#print(data.describe())
#what the some numbers let us of release_year since that is the only int64 type
#the mean is 2014.18 so that could be the average year of these productions where released. 2014 is quite a popular year for film arts
#the min is 1925.000 so the oldest production was in the year 1925, we can check that by sorting the list ascending 
# and call .head() just to make it quicker and not receive the whole list

years = (data.sort_values(by='release_year', ascending=True))
#print(years.head())
#1925 is the correct, the oldest film in netflix is Pioneers: Filmmakers

#now let's do the max
#the most recent year is 2021, let's check
#print(years.tail())
#2021 is the correct year as the last 5 of the sorted list are published in 2021

#Alright! Have some fun with this. Let's say we have a family movie night. What do we have in listed_in to get a family-friendly movie/TV show?
family_movies = data[(data['listed_in'].str.contains('Family'))]
#print(family_movies)
#so we are down to 641 choices, let's decide to watch a movie by justing get the first 5 of the list
print(family_movies['title'].head())
#so the movies that pop up are:
#1. My Little Pony: A New Generation
#2. Confessions of an Invisible Girl
#3. Go! Go! Cory Carson: Chrissy Takes the Wheel
#4. Nightbooks
#5. A StoryBots Space Adventure

#indecisive? let's do a random pick
#results may differ
rand = random.randint(1,5)
print(rand)

#I got 4 so I'm watching Nightbooks. 
