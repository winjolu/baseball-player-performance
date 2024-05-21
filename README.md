# Baseball Player Performance Analysis

## Overview

This project, developed by Winston Ludlam, a freelance data analyst, aims to analyze and visualize the performance of baseball players using historical data. The goal is to uncover insights into player performance metrics, salary distributions, and factors influencing Hall of Fame inductions.

## Objectives

The primary objectives of this project are:
1. To understand the relationship between various performance metrics and player salaries.
2. To identify key performance indicators that correlate with higher salaries.
3. To analyze the characteristics and performance metrics of Hall of Fame inductees.
4. To cluster players based on their performance metrics for further insights.

## Methodology

### Data Collection

The data used in this analysis comes from historical baseball performance records, including:
- Batting statistics
- Pitching statistics
- Fielding statistics
- Salary data
- Hall of Fame induction records
- Consumer Price Index (CPI) for salary adjustment

### Research Questions

1. What are the key performance metrics that correlate with higher player salaries?
2. How do the performance metrics of Hall of Fame inductees differ from non-inductees?
3. Can we cluster players into meaningful groups based on their performance metrics?
4. How have player salaries evolved over time when adjusted for inflation?

### Analysis and Visualization

#### Data Cleaning and Preprocessing
- Merging multiple data sources.
- Filtering data to include only relevant years (1920-2013).
- Adjusting salaries for inflation using CPI data.
- Handling missing values and outliers.

#### Correlation Analysis
- Calculating and visualizing the correlation matrix to identify relationships between performance metrics and salaries.

#### Regression Analysis
- Performing regression analysis to quantify the impact of specific performance metrics on salaries.
- Visualizing regression results to highlight significant predictors.

#### Cluster Analysis
- Applying clustering algorithms (e.g., K-Means) to group players based on performance metrics.
- Visualizing clusters using dimensionality reduction techniques (e.g., PCA).

#### Hall of Fame Analysis
- Comparing the performance metrics of Hall of Fame inductees with non-inductees.
- Visualizing distributions of key metrics for inductees and non-inductees.

## Conclusions

The analysis reveals several key insights:

1. **Salary Correlations**: Certain performance metrics, such as strikeouts (SO), wins (W), and innings pitched (IPouts), show a strong positive correlation with player salaries.
2. **Regression Findings**: Regression analysis indicates that metrics like batting average and OPS have a significant impact on salaries, highlighting their importance in player valuation.
3. **Cluster Insights**: Clustering players based on performance metrics helps in identifying groups of players with similar characteristics, providing a deeper understanding of player types.
4. **Hall of Fame Characteristics**: Hall of Fame inductees generally exhibit superior performance metrics compared to non-inductees, with notable differences in key statistics like home runs (HR) and earned run average (ERA).

## File Structure
```
baseball-player-performance/
├── data/
│   ├── core/
│   │   ├── Batting.csv
│   │   ├── Pitching.csv
│   │   ├── Fielding.csv
│   │   ├── People.csv
│   ├── contrib/
│   │   ├── Salaries.csv
│   │   ├── HallOfFame.csv
│   ├── cpi.csv
│   ├── performance_data.parquet
├── notebooks/
│   ├── eda.ipynb
├── scripts/
│   ├── data_preparation.py
├── LICENSE
├── README.md
```


## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This developer gratefully acknowledges:
- The [Lahman Baseball Database](http://seanlahman.com/) for providing the historical baseball data.
- The [US Bureau of Labor Statistics](https://www.bls.gov/) for CPI data.
- Professor Rick White at MiraCosta College for his guidance and support.
- All the ball players who have been joyfully generating these data and the statisticians (both amateur and professional) who have been faithfully compiling and querying the database for more than 180 years.
