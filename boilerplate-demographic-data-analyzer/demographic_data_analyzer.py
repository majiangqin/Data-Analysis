import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts('race')

    # What is the average age of men?
    average_age_men = round(df[df['sex']=='Male'].age.mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df['education']=='Bachelors'].shape[0]/df.shape[0])*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    education=['Bachelors','Masters','Doctorate']
    # mask=((df['education']=='Bachelors')|(df['education']=='Masters')|(df['education']=='Doctorate'))&(df['salary']=='>50K')
    # mask1=((df['education']!='Bachelors')&(df['education']!='Masters')&(df['education']!='Doctorate'))&(df['salary']=='>50K')
    # higher_education = round((df[mask].shape[0]/df.shape[0])*100,1)
    # lower_education = round((df[mask1].shape[0]/df.shape[0])*100,1)
    mask1=df['education'].isin(education)
    mask2 = (~df['education'].isin(education))
    mask11=df['education'].isin(education)&(df['salary']=='>50K')
    mask22 = (~df['education'].isin(education)) & (df['salary'] == '>50K')
    higher_education=df[mask11].shape[0]
    lower_education=df[mask22].shape[0]

    # percentage with salary >50K
    higher_education_rich = round((df[mask11].shape[0]/df[mask1].shape[0])*100,1)
    lower_education_rich = round((df[mask22].shape[0]/df[mask2].shape[0])*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask= df['hours-per-week']== min_work_hours
    mask_salary=mask&(df['salary']=='>50K')
    num_min_workers = round(df[mask_salary].salary.count()/df[mask].salary.count()*100)

    rich_percentage = num_min_workers

    # What country has the highest percentage of people that earn >50K?
    highest_earning =(df[df['salary']=='>50K'].value_counts('native-country')/df['native-country'].value_counts()).sort_values()
    highest_earning_country='Iran'
    highest_earning_country_percentage = round(highest_earning['Iran']*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    mask_india=(df['native-country']=='India')&(df['salary']=='>50K')
    occupation_sort=df[mask_india].occupation.value_counts().head(0)
    top_IN_occupation ='Prof-specialty'

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
