# StockX-Sneaker-Notifier

This Python script monitors StockX for sneakers and sends updates to a Discord webhook based on specified criteria.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone this repository or download the script.
2. Install the required libraries using the following command:
pip install requests beautifulsoup4 re

css
Copy code
3. Create a `config.json` file in the same directory with the following format:
```json
{
    "Shoe name": "shoe-name",
    "Start page": 1,
    "Stop page": 10,
    "Size": "size",
    "Desired profit": 100,
    "Webhook": "your-discord-webhook-url"
}
Usage
Run the script using the following command:
Copy code
python script.py
The script will loop through different years and pages on StockX, fetch sneaker data, and send updates to the Discord webhook if the profit margin is higher than the desired value.
Configuration
Shoe name: The name of the sneaker you want to monitor.
Start page: The page number to start monitoring on StockX.
Stop page: The page number to stop monitoring on StockX.
Size: The shoe size you're interested in.
Desired profit: The minimum profit margin to trigger an update.
Webhook: Your Discord webhook URL to receive updates.
Discord Notifications
The script sends updates to a Discord webhook in the form of an embed containing the sneaker information.

Disclaimer
This script is intended for educational purposes and personal use. Use responsibly and ensure you adhere to the terms of service of StockX and Discord.
