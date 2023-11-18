# main.py in market_trends_analysis folder

from data_aggregator import aggregate_data
from query_processor import process_query
from data_analyzer import analyze_data

def main():
    user_query = "Ice cream trends in Edmonton"
    topics = process_query(user_query)
    aggregated_data = aggregate_data()
    trends = analyze_data(aggregated_data)

    # Display or further process the trends
    print(trends)

if __name__ == "__main__":
    main()
