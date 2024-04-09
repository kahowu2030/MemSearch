import schedule
import time
from datetime import datetime, timedelta
from analyze_usage_behavior import analyze_usage_behavior


def analyze_previous_day_usage():
    # Get the previous day's date
    previous_day = datetime.now().date() - timedelta(days=1)
    previous_day_str = previous_day.strftime('%Y-%m-%d')
    
    # Construct the CSV file path for the previous day
    csv_file_path = f'usage_data/{previous_day_str}.csv'
    summary_file_path = f'usage_data/{previous_day_str}_summary.txt'
    
    # Call the analyze_usage_behavior function with the CSV file path
    analyze_usage_behavior(csv_file_path, summary_file_path)

def schedule_analysis():
    # Schedule the analysis to run every day at 12am
    schedule.every().day.at("00:00").do(analyze_previous_day_usage)
    
    while True:
        # Run pending scheduled tasks
        schedule.run_pending()
        time.sleep(1)

# analyze today's usage
def analyze_today_usage():
    # Get the previous day's date
    today = datetime.now().date()
    today_str = today.strftime('%Y-%m-%d')
    
    # Construct the CSV file path for the previous day
    csv_file_path = f'usage_data/{today_str}.csv'
    summary_file_path = f'usage_data/{today_str}_summary.txt'
    
    # Call the analyze_usage_behavior function with the CSV file path
    analyze_usage_behavior(csv_file_path, summary_file_path)

analyze_previous_day_usage()
analyze_today_usage()

# Start scheduling the analysis
# schedule_analysis()