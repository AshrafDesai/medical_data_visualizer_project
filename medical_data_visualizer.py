import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import the dataset
df = pd.read_csv('medical_examination.csv')

# 1. Add an overweight column
# BMI = weight / (height in meters)^2
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)

# 2. Normalize data
# If cholesterol or gluc is 1 -> 0 (good), else -> 1 (bad)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Functions to draw plots
def draw_cat_plot():
    # 3. Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 4. Group and reformat data to show counts
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']) \
                   .size() \
                   .reset_index(name='total')

    # 5. Draw the categorical plot using seaborn
    fig = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    ).fig

    # Return the figure
    return fig

def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        vmax=0.3,
        vmin=-0.1,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5}
    )

    return fig

# Optional: test plots
if __name__ == "__main__":
    cat_fig = draw_cat_plot()
    cat_fig.savefig("catplot.png")
    heat_fig = draw_heat_map()
    heat_fig.savefig("heatmap.png")
    print("Plots saved as catplot.png and heatmap.png")
