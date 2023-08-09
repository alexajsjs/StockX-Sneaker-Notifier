# StockX-Sneaker-Notifier

This Python script monitors StockX for sneakers and sends updates to a Discord webhook based on specified criteria.

## Requirements

- Python 3.11 or further
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
```

## Usage

Run the script using the following command:
Copy code
python script.py
The script will loop through different years and pages on StockX, fetch sneaker data, and send updates to the Discord webhook if the profit margin is higher than the desired value.
## Configuration
Shoe name: The name of the sneaker you want to monitor.
Start page: The page number to start monitoring on StockX.
Stop page: The page number to stop monitoring on StockX.
Size: The shoe size you're interested in.
Desired profit: The minimum profit margin to trigger an update.
Webhook: Your Discord webhook URL to receive updates.
## Discord Notifications
The script sends updates to a Discord webhook in the form of an embed containing the sneaker information.

## Disclaimer

This script is intended for educational purposes and personal use. Use responsibly and ensure you adhere to the terms of service of StockX and Discord.

## MIT License

Copyright (c) [2023] [Crazy cool]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
