# Amazon Price Tracker

## Description
This program extracts product details such as **name, price, rating, availability, and review count** for a specific category of products (e.g., keyboards) from Amazon. It scrapes the data and stores it in a structured format (CSV/Excel) for further analysis.

## Features
- Extracts product **title**, **price**, **rating**, **review count**, and **availability**.
- Supports scraping for a **specific niche category** of products.
- Saves extracted data in **CSV** and **Excel** formats.
- Handles missing values and cleans the data before saving.

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed and the following dependencies:
```sh
pip install requests beautifulsoup4 pandas numpy openpyxl
```

## Usage
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/Amazon-price-tracker.git
   cd Amazon-price-tracker
   ```

2. Run the script:
   ```sh
   python main.py
   ```

3. The extracted data will be saved as `amazon_data.csv` and `amazon_data.xlsx`.

## Output
The script saves the extracted data in **CSV and Excel** formats with the following columns:
- **Title**: Name of the product
- **Price**: Product price (if available)
- **Rating**: Customer rating
- **Reviews**: Number of reviews
- **Availability**: Stock availability

## Notes
- Amazon uses dynamic content loading, so ensure your request headers mimic a real browser to avoid being blocked.
- This script may require updates if Amazon changes its website structure.


## Disclaimer
This project is for **educational purposes only**. Scraping Amazon may violate their **Terms of Service**. Use it responsibly.

---

