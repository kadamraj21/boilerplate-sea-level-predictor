import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points')

    # Line of best fit (1880–2050)
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_future = pd.Series(range(1880, 2051))
    y_future = result.slope * x_future + result.intercept
    ax.plot(x_future, y_future, 'r', label='Best Fit: 1880–2050')

    # Line of best fit (2000–2050)
    df_recent = df[df['Year'] >= 2000]
    result_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = result_recent.slope * x_recent + result_recent.intercept
    ax.plot(x_recent, y_recent, 'g', label='Best Fit: 2000–2050')

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    ax.grid(True)

    # Save and return Axes
    fig.tight_layout()
    fig.savefig('sea_level_plot.png')
    return ax  # ✅ Must return ax, not fig
