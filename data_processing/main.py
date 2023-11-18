# main.py
from market_trend_scraper import aggregate_scraping_results
from trend_analysis import analyze_trends
from trend_prediction import predict_future_trends

def main():
    user_query = "Ice cream trends in Edmonton"
    topics = extract_topics(user_query)
    print(f"Extracted Topics: {topics}")

    scraped_data = scrape_edmonton_journal()
    analyze_trends(scraped_data)

if __name__ == "__main__":
    main()
