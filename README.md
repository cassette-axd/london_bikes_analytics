# London Bikes Dashboard

## Objective
To support data-driven storytelling, athlete development, and performance analysis by identifying trends and standout achievements from the 2021 Tokyo Olympics. 
This project uses key performance indicators like medal counts, country representation, gender distribution, and sport categories to extract meaningful insights from the Games.

## Challenges
Working with the official Olympic dataset involved several data-related hurdles:

- Non-standardized formatting of athlete names, disciplines, and event names.

- Multiple entries per athlete (e.g., for team events or multiple medals).

- Medal duplication and aggregation issues for events with shared medals (e.g., team events).

- Data completeness—some fields like age or height were missing or not included in the dataset.

- Difficulty comparing across disciplines, since events vary greatly in structure and scoring.

## Solution
Built an interactive data dashboard and backend workflow that integrates CSV data, Python (Pandas) for preprocessing, SQL for structured querying, and Tableau for visual presentation. This tool provides:

- Top athletes by total medal count, including filters by sport and gender

- Country-wise medal distribution, including comparisons by population or team size

- Most competitive sports based on number of participants and medal spread

- Gender distribution across sports and events

- Summary dashboards for stakeholders to explore participation trends and medal efficiency

This dashboard empowers coaches, analysts, journalists, and Olympic committees to gain fast, intuitive insights from a historically rich and complex dataset.

## Tools and Technologies
- Excel: Initial data collection and cleaning

- Python: Data preprocessing and automation

- Tableau: Interactive dashboard and report creation

## Features
- Clean and intuitive visual interface

- Filtering by metric (medal count, sport, gender, participant count, etc.)

- Ability to compare athletes, countries, and events across performance metrics

- Real-time updating capability (when connected to refreshed datasets)
