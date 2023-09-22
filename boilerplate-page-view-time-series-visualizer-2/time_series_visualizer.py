import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'],index_col='date')

# Clean data
value1=df['value'].quantile(0.975)
value2=df['value'].quantile(0.025)
mask=(df['value']<value1)&(df['value']>value2)
df = df[mask]


def draw_line_plot():
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.plot(df.index,df['value'],c='red',linewidth=1)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot

    # df_bar = df.groupby(pd.Grouper(freq='M')).mean()

    df['day']=df.index.day
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar=df.groupby(['year','month'],as_index=False).value.mean()
    # df_bar['month'] = np.where(df_bar['month'] == 1, 'January', df_bar['month'])
    # df_bar['month'] = np.where(df_bar['month'] == '2', 'February', df_bar['month'])
    # df_bar['month'] = np.where(df_bar['month'] == '3', 'March', df_bar['month'])
    # df_bar['month'] = np.where(df_bar['month'] == '4', 'April', df_bar['month'])
    # df_bar['month'] = np.where(df_bar['month'] == '5', 'May', df_bar['month'])
    # df_bar['month'] = np.where(df_bar['month'] == '6', 'June', df_bar['month'])
    # df_bar['month'] = np.where(df_bar['month'] == '7', 'July', df_bar['month'])
    # df_bar['month'] = np.where(df_bar['month'] == '8', 'August', df_bar['month'])
    # df_bar['month'] = np.where(df_bar['month'] == '9', 'December', df_bar['month'])
    # df_bar['month'] = np.where(df_bar['month'] == '10', 'October', df_bar['month'])
    #
    # df_bar['month'] = np.where(df_bar['month'] == '11', 'November', df_bar['month'])
    # df_bar['month'] = np.where(df_bar['month'] == '12', 'December', df_bar['month'])

    # Convert month numbers to month names
    df_bar['month'] = df_bar['month'].replace({
        1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
        7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
    })
    month_order=['January','February','March', 'April','May','June','July', 'August',  'September', 'October',  'November',  'December']
    df_bar['month']=pd.Categorical(df_bar['month'],categories=month_order,ordered=True)
    # Draw bar plot
    fig=plt.figure(figsize=(10,8))
    ax=fig.add_subplot(1,1,1)
    sns.barplot(x='year', y='value', data=df_bar,hue='month',palette='rainbow')

    ax.set_xlabel('Years',fontsize=10)
    ax.set_ylabel('Average Page Views')
    ax.tick_params(axis='x',rotation=45,labelsize=10)
    plt.legend(loc='upper left')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    # df_box = df.copy()
    # df_box.reset_index(inplace=True)
    # df_box['year'] = [d.year for d in df_box.date]
    # df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df['day']=df.index.day
    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar=df.groupby(['year','month'],as_index=False).value.value_counts()
    # Convert month numbers to month names
    df_bar['month'] = df_bar['month'].replace({
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    })
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
                   'Nov', 'Dec']
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=month_order, ordered=True)

    # Draw box plots (using Seaborn)
    plt.figure()
    fig,[ax1,ax2]=plt.subplots(1,2,figsize=[15,8])
    sns.boxplot(x='year',y='value',data=df_bar,ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page View')

    sns.boxplot(x='month',y='value',data=df_bar,ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page View')

    plt.tight_layout()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
