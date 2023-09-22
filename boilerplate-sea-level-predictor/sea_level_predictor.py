import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    data=pd.read_csv('epa-sea-level.csv')
    x=data['Year']
    y=data['CSIRO Adjusted Sea Level']
    new_year=np.arange(2014,2051)
    ser_year=pd.Series(new_year)
    x_new=pd.concat([x,ser_year],axis=0)

    res = linregress(x, y)



    # Create scatter plot
    plt.figure()
    plt.scatter(x=data['Year'],y=data['CSIRO Adjusted Sea Level'],label='original data')




    # Create first line of best fit
    plt.plot(x_new,res.intercept+res.slope*x_new,'r',label='fitted line')


    # Create second line of best fit
    mask=x>=2000
    x_second=data[mask]
    x=x_second['Year']
    y=x_second['CSIRO Adjusted Sea Level']
    res=linregress(x,y)

    xx=pd.concat([x,ser_year])
    plt.plot(xx,res.intercept+res.slope*xx,'r',label='new fitted line')

    # Add labels and title
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    plt.title('Rise in Sea Level')
    plt.legend()


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()



#
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.stats import linregress
# import numpy as np
#
# def draw_plot():
#     # Read data from file
#     data = pd.read_csv('epa-sea-level.csv')
#
#     # Create scatter plot
#     plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])
#
#     # Calculate linear regression for the entire dataset
#     slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
#
#     # Create an array of years from 1880 to 2050
#     years = np.arange(1880, 2051)
#
#     # Plot the line of best fit for the entire dataset
#     plt.plot(years, intercept + slope * years, 'r', label='Best Fit Line (1880-2050)')
#
#     # Filter data for years from 2000 to the most recent year
#     recent_data = data[data['Year'] >= 2000]
#
#     # Calculate linear regression for recent data
#     slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
#
#     # Create an array of years from 2000 to 2050 for the second line of best fit
#     years_recent = np.arange(2000, 2051)
#
#     # Plot the new line of best fit for recent data
#     plt.plot(years_recent, intercept_recent + slope_recent * years_recent, 'b', label='Best Fit Line (2000-2050)')
#
#     # Add labels and title
#     plt.xlabel('Year')
#     plt.ylabel('Sea Level (inches)')
#     plt.title('Rise in Sea Level')
#
#     # Add legend
#     plt.legend()
#
#     # Save plot and return data for testing (DO NOT MODIFY)
#     plt.savefig('sea_level_plot.png')
#     return plt.gca()


