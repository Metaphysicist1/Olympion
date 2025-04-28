import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from matplotlib.colors import Normalize

# Set the style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("colorblind")

def load_data():
    """Load and prepare the Olympic datasets."""
    # Load athletes data
    athletes_df = pd.read_csv("data/athletes.csv")
    
    # Load games data
    games_df = pd.read_csv("data/games.csv", sep=";")
    
    # Load results data from Excel
    results_path = "data/results.xlsx"
    xls = pd.ExcelFile(results_path)
    
    # Load all sheets and concat them
    dataframes = []
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(results_path, sheet_name=sheet_name)
        df.columns = df.iloc[0]  # Set first row as column names
        df = df.iloc[1:].reset_index(drop=True)  # Remove header row
        dataframes.append(df)
    
    results_df = pd.concat(dataframes, ignore_index=True)
    
    # Convert athlete_id to string to facilitate merging
    athletes_df['athlete_id'] = athletes_df['athlete_id'].astype(str)
    results_df['athlete_id'] = results_df['athlete_id'].astype(str)
    
    return athletes_df, games_df, results_df

def analyze_medals_vs_population_gdp():
    """Analyze and visualize the relationship between medals and country metrics."""
    # Load medal data
    medal_table = pd.read_csv("data/medal_table_2012.csv")
    
    # Load GDP and population data
    gdp_pop_df = pd.read_csv("data/gdp_pop_2012.csv")
    
    # Join datasets - first create a country code mapping
    # Olympic country codes often differ from standard ISO codes
    # For this example, we'll create a mapping based on country names
    merged_df = pd.merge(
        medal_table, 
        gdp_pop_df,
        left_on='country',
        right_on='country',
        how='left'
    )
    
    # Create visualization for medals per capita
    plt.figure(figsize=(14, 8))
    
    # Calculate medals per million people
    merged_df['total_medals'] = merged_df['gold'] + merged_df['silver'] + merged_df['bronze']
    merged_df['medals_per_million'] = merged_df['total_medals'] / (merged_df['population'] / 1000000)
    
    # Filter out countries with no population data
    filtered_df = merged_df[merged_df['population'].notna() & (merged_df['total_medals'] > 0)]
    
    # Select top 20 countries by medals per capita for better visualization
    top_per_capita = filtered_df.sort_values('medals_per_million', ascending=False).head(20)
    
    # Create the bar chart
    ax = sns.barplot(
        x='country_code', 
        y='medals_per_million', 
        data=top_per_capita,
        palette='viridis'
    )
    
    # Add color to bars based on total medals
    norm = Normalize(top_per_capita['total_medals'].min(), top_per_capita['total_medals'].max())
    sm = plt.cm.ScalarMappable(cmap="viridis", norm=norm)
    sm.set_array([])
    
    # Customize the chart
    plt.title('Olympic Efficiency: Medals Per Million Population (2012 Olympics)', fontsize=16)
    plt.xlabel('Country', fontsize=14)
    plt.ylabel('Medals Per Million People', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Add a color bar to show total medals
    cbar = plt.colorbar(sm)
    cbar.set_label('Total Medals', fontsize=12)
    
    # Add annotation for top 3 countries
    for i in range(3):
        row = top_per_capita.iloc[i]
        plt.annotate(
            f"{row['medals_per_million']:.2f} medals per million\n{row['total_medals']} total medals",
            xy=(i, row['medals_per_million']),
            xytext=(0, 20),
            textcoords='offset points',
            ha='center',
            va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2')
        )
    
    # Save the figure
    plt.savefig('medals_per_capita_2012.png', dpi=300, bbox_inches='tight')
    print("Visualization saved as 'medals_per_capita_2012.png'")

if __name__ == "__main__":
    print("Analyzing Olympic data...")
    analyze_medals_vs_population_gdp()
    print("Analysis complete!") 