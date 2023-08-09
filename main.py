import requests as req
from bs4 import BeautifulSoup
import sys
import re
import json

# Reconfiguring our output
sys.stdout.reconfigure(encoding = "utf-8")

# General variables
config = json.loads(open("config.json", "r").read())
shoe_name = config["Shoe name"]
start_page = config["Start page"]
stop_page = config["Stop page"]
size = config["Size"]
desired_profit = config["Desired profit"]
webhook = config["Webhook"]

# Functions
def send_to_discord(webhook, link, description, img_url, l_a, a_p, p_m):
    
    # Embed values
    values = {
        "embeds": [
            {
            "id": 430907797,
            "description": description,
            "fields": [],
            "url": link,
            "image": {
                "url": img_url
            },
            "title": "NEW SHOE",
            "color": 16711680
            },
            {
            "id": 611814474,
            "description": l_a,
            "fields": [],
            "title": "Lowest Ask"
            },
            {
            "id": 446085990,
            "description": a_p,
            "fields": [],
            "title": "Average Price"
            },
            {
            "id": 605653094,
            "description": p_m,
            "fields": [],
            "title": "Profit Margin"
            }
        ],
        "components": [],
        "actions": {},
        "username": "SNEAKER"
        }
    
    req.post(webhook, json=values)

# Looping through the years
for i in range(1, 24):
    year = 2024 - i
    print(year)

    # Main loop
    for page in range(start_page, stop_page):
        print(f"Page: {page}")

        stx_url = f"https://stockx.com/search/sneakers/size-{size}/most-expensive{shoe_name}?years={year}&page={page}"

        # Getting the pages html data
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        stx_html = req.get(stx_url, headers=headers).text
        parsed_html = BeautifulSoup(stx_html, "html.parser")

        # Variables for the shoe descriptors
        individual_la = parsed_html.find_all(class_="chakra-text css-nsvdd9")
        individual_names = parsed_html.find_all(class_="chakra-text css-3lpefb")
        individual_ap = parsed_html.find_all(class_="css-1ny2kle")
        links = parsed_html.find_all(class_="css-pnc6ci")

        # Regex patterns
        ap_la_pattern = re.compile(r"\$\d*,\d*|\$\d*")
        name_pattern = re.compile(r">.*<")
        link_pattern = re.compile(r'f="\S+"')
        img_pattern = re.compile(r'src="\S*"')

        # Main program(Sorting data)
        for i in range(len(individual_la)):
            # Individual shoe data
            lowest_ask = str(individual_la[i])
            name = str(individual_names[i])
            average_price = str(individual_ap[i])
        
            # Calculating price difference
            try:
                profit_margin = int(ap_la_pattern.findall(average_price)[0][1::].replace(",", "")) - int(ap_la_pattern.findall(lowest_ask)[0][1::].replace(",", ""))
            except IndexError:
                profit_margin = "Unknown"

            # Main statement
            try:
                if profit_margin > desired_profit:

                    # Data used for Discord
                    uf_link = link_pattern.findall(str(links[i]))[0]

                    link = uf_link[3:len(uf_link)-1]
                    img = f"https://images.stockx.com/images/{link}.jpg?fit=fill&amp;bg=FFFFFF&amp;w=140&amp;h=75&amp;fm=avif&amp;auto=compress&amp;dpr=4&amp"
                    
                    # Printed data
                    print(f"Shoe:[{name_pattern.findall(name)[0]}] Lowest Ask:[{ap_la_pattern.findall(lowest_ask)[0]}] Average Price:[{ap_la_pattern.findall(average_price)[0]}]")
                    print(f"Profit: {profit_margin}")

                    # Sending data to discord
                    send_to_discord(webhook=webhook, link=f"https://stockx.com{link}", description=name_pattern.findall(name)[0], img_url=img, l_a=ap_la_pattern.findall(lowest_ask)[0], a_p=ap_la_pattern.findall(average_price)[0], p_m = profit_margin)
            except TypeError:
                continue
