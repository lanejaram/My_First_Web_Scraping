CityMall Myanmar Electronics Web Scraper
A Python web scraper that extracts product names and prices from the Electronics category of CityMall Myanmar's online store.

Features
Automatic Pagination: Scrapes multiple pages of product listings

Robust Error Handling: Implements retry logic with exponential backoff for failed requests

Progress Tracking: Uses tqdm for real-time progress visualization

Data Export: Saves extracted data to Excel files with timestamps

User-Agent Rotation: Mimics browser requests to avoid blocking

Installation
Prerequisites
Python 3.7+

pip package manager

Install Required Libraries
bash
pip install requests beautifulsoup4 pandas tqdm html5lib
Usage
Basic Usage
python
python scraper.py
The script will:

Extract product data from the first 20 pages of the Electronics category

Save the data to an Excel file with a timestamp (e.g., Output 14-30-45.xlsx)

Configuration
You can modify the following in the script:

Number of pages to scrape: Change range(0, 20+1) in the main() function

Target URL: Modify the base URL in the main() function

Delay between requests: Adjust time.sleep(0) in the main loop

Project Structure
Main Functions
extract_last_page_number():

Extracts the total number of pages available for the category

Note: Currently commented out in the main function

extract_product_name(tag):

Extracts product names from HTML tags

Handles the product name element structure

extract_product_price(tag):

Extracts product prices from HTML tags

Handles both regular and sale prices

Cleans price data (removes "Ks" and commas)

main():

Main execution function

Manages pagination, data extraction, and file export

Data Output
The script creates an Excel file containing:

Product Name: Name of the electronics product

Product Price: Cleaned price (numeric format)

Error Handling
The script includes several error handling features:

Retry Mechanism: Retries failed requests up to 5 times

HTTP Status Codes: Handles 429, 500, 502, 503, and 504 errors

Timeout: 30-second timeout for requests

Exception Handling: Graceful handling of missing elements

Dependencies
requests: HTTP requests

beautifulsoup4: HTML parsing

pandas: Data manipulation and Excel export

tqdm: Progress bar

html5lib: HTML parser

urllib3: HTTP client utilities

Important Notes
Legal Considerations
This script is for educational purposes only

Check CityMall's Terms of Service and robots.txt before use

Respect website's crawling policies and rate limits

Consider adding delays between requests to avoid overloading servers

Technical Notes
The script uses a custom User-Agent header to mimic a browser

HTML5 parser is used for better compatibility with modern websites

Session management is implemented for connection pooling

Customization
To scrape different categories:

Update the base URL in the main() function

Adjust the CSS selectors in the extraction functions if needed

Troubleshooting
Common Issues
Connection Errors:

Check internet connection

Verify the target URL is accessible

Blocked Requests:

Increase delays between requests

Rotate User-Agent strings

Use proxy servers if necessary

Missing Data:

Verify CSS selectors are still valid

Check if website structure has changed

Contributing
Feel free to fork this project and submit pull requests with improvements.

License
This project is for educational purposes. Use responsibly and in accordance with the target website's terms of service.

Disclaimer
This tool is intended for educational purposes only. The authors are not responsible for any misuse or damages caused by this software. Always respect websites' terms of service and robots.txt files.
