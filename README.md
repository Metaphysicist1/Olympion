# Olympion

# Olympion: Olympic Games Data Analysis

Welcome to Olympion! This project focuses on analyzing data related to the Olympic Games. We will explore various datasets to gain insights into athletes' performances, medal distributions, and more.

## Project Overview

### Information

You are provided with several data files related to the Olympic Games:

- **athletes.csv**: Contains biographic data on athletes, such as their names and dates of birth.
- **results.xlsx**: An Excel file containing information about individual results of athletes in the Olympic Games of different years. Each tab holds information for one year, including the sports, events, positions, and medals achieved.
- **games.csv**: Contains information about the Olympic Games, such as their locations and opening dates.

For more details on the data, refer to the following sources: [athletes](#), [games](#), [results](#). Note that some minor processing steps have been carried out, so the data may not be 100% identical to the data on the website.

### Exercises

#### Exercise 1: Data Preparation

1. **Read and Inspect Data**: Read in all datasets and inspect their basic properties.
2. **Combine Data**: Merge, concatenate, or reshape the data into a single, tidy dataset to answer subsequent questions.
3. **Describe Processing Steps**: Justify your data processing steps, highlighting the main challenges and how you dealt with them.
4. **Sort and Display Data**: Sort the data permanently by year, sport, event, and position. Display the first 3 rows and print the number of rows and columns.

**Notes**:
- Avoid redundancies in your code.
- Further data processing steps may be required for subsequent exercises.

#### Exercise 2: Basic Analysis

1. **Most Common Last Name (2012 Olympics)**: Identify the most common last name among athletes in the 2012 Olympic Games and its frequency.
2. **Gold Medal Winner (100m Race, 2012 Olympics)**: Determine the woman who won the gold medal in the 100 meters race in the 2012 Olympic Games.
3. **Most Gold Medals (Specific Countries)**: Identify the athlete with the most gold medals from the following countries: Jamaica, Trinidad and Tobago, Barbados, Grenada, Saint Kitts and Nevis.
4. **Mongolia's Performance**: Determine the best, worst, and median positions achieved by athletes from Mongolia.

#### Exercise 3: Advanced Analysis

1. **Highest Average Age of Gold Medal Winners**: Identify the 5 sports with the highest average age of gold medal winners.
2. **Body-Mass-Index (BMI) Analysis**: Derive a new column for BMI and identify the 5 sports with the lowest average BMI of male athletes.

#### Exercise 4: Medal Table (2012 Olympics)

Calculate the medal table for the 2012 Olympic Games. The table should have the same structure as the official medal table. Display the top 10 countries.

**Hint**: In team events, each medal should count only once for the medal table.

#### Exercise 5: Data Visualization

1. **Identify a Pattern**: Identify an interesting pattern, trend, or relationship in the data and create a visualization to communicate this insight.
2. **Describe the Visualization**: Briefly describe what the visualization shows and explain why the pattern is interesting or surprising.

## Getting Started

Follow these steps to set up the project on your local machine.

### Prerequisites

Make sure you have the following installed:
- Git
- Python (with pandas, numpy, matplotlib, and other necessary libraries)

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Metaphysicist1/Olympion.git
