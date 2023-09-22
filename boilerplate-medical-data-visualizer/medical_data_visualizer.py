import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
mask = df['weight'] / ((df['height'] * 0.01) ** 2)
df['overweight'] = np.where(mask > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    df_cat = df_cat.groupby(['cardio', 'value'], as_index=False).variable.value_counts()

    # Draw the catplot with 'sns.catplot()'
    df_cat.rename(columns={'count': 'total'}, inplace='True')

    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x='variable', y='total', col='cardio', kind='bar', hue='value')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    mask_a = (df['ap_lo'] <= df['ap_hi'])
    mask_b = (df['height'] >= df['height'].quantile(0.025))
    mask_c = (df['height'] <= df['height'].quantile(0.975))
    mask_d = (df['weight'] >= df['weight'].quantile(0.025))
    mask_e = (df['weight'] <= df['weight'].quantile(0.975))

    df_heat = df[mask_a & mask_b & mask_c & mask_d & mask_e]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    # ax=sns.heatmap(corr,mask=mask)
    # for i in range(len(corr)):
    #     for j in range(len(corr)):
    #         if i<j:
    #             plt.text(i+0.5,j+0.5,f'{corr.iloc[i,j]:.1f}',va='center',ha='center')
    sns.heatmap(corr,mask=mask,center=0,annot=True,fmt='.1f')
    ax.tick_params(axis='both', labelsize=8)
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
