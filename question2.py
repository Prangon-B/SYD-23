import os
import pandas as pd

def get_season_months():
    return {
        'Summer': ['December', 'January', 'February'],
        'Autumn': ['March', 'April', 'May'],
        'Winter': ['June', 'July', 'August'],
        'Spring': ['September', 'October', 'November']
    }

def analyze_temperature_data(input_folder, output_folder):
    all_data = pd.DataFrame()

    #combine all CSV files
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            filepath = os.path.join(input_folder, filename)
            df = pd.read_csv(filepath)
            all_data = pd.concat([all_data, df], ignore_index=True)

    #average temperatures for each season
    season_months = get_season_months()
    season_averages = {}
    for season, months in season_months.items():
        season_averages[season] = all_data[months].mean(axis=1)
    season_avg_df = pd.DataFrame(season_averages)
    season_avg_df = season_avg_df.mean().to_frame(name='AverageTemperature')
    season_avg_df.to_csv(os.path.join(output_folder, "average_temp.txt"))

    #stations with largest temperature range 
    monthly_cols = list(get_season_months().values())
    flat_months = [month for sublist in monthly_cols for month in sublist]
    temp_range = all_data[flat_months].max(axis=1) - all_data[flat_months].min(axis=1)
    all_data['TempRange'] = temp_range
    max_range = temp_range.max()
    largest_range_stations = all_data[all_data['TempRange'] == max_range][['STATION_NAME', 'TempRange']]
    largest_range_stations.to_csv(os.path.join(output_folder, "largest_temp_range_station.txt"), index=False)

    #warmest and coolest stations
    all_data['YearlyAverage'] = all_data[flat_months].mean(axis=1)
    max_avg = all_data['YearlyAverage'].max()
    min_avg = all_data['YearlyAverage'].min()
    result = all_data[all_data['YearlyAverage'].isin([max_avg, min_avg])][['STATION_NAME', 'YearlyAverage']]
    result.to_csv(os.path.join(output_folder, "warmest_and_coolest_station.txt"), index=False)

def main():
    input_folder = r"D:\CDU\hit137\HIT137 Assignment 2 S1 2025\temperature_data"
    output_folder = r"D:\CDU\hit137\HIT137 Assignment 2 S1 2025"
    analyze_temperature_data(input_folder, output_folder)

if __name__ == "__main__":
    main()
