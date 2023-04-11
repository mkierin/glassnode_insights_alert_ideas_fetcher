import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of webpages to extract data from
webpages = ['https://insights.glassnode.com/the-week-onchain-week-10-2023/',
            'https://insights.glassnode.com/the-week-onchain-week-12-2023/',
            'https://insights.glassnode.com/the-week-onchain-week-08-2023/',
            'https://insights.glassnode.com/the-week-onchain-week-05-2023/',
            'https://insights.glassnode.com/the-week-onchain-week-3-2023/',
            'https://insights.glassnode.com/the-week-onchain-week-06-2023/',
            'https://insights.glassnode.com/the-week-onchain-week-07-2023/',
            'https://insights.glassnode.com/the-week-onchain-week-2-2023/',
            'https://insights.glassnode.com/the-week-onchain-week-09-2023/',
            'https://insights.glassnode.com/the-week-onchain-week-13-2023/',
            'https://insights.glassnode.com/the-week-onchain-week-31-2022/',
            'https://insights.glassnode.com/the-week-onchain-week-14-2023/',
            'https://insights.glassnode.com/the-week-onchain-week-34-2022/',
            'https://insights.glassnode.com/the-week-onchain-week-35-2022/',
            'https://insights.glassnode.com/the-week-onchain-week-04-2023/',
            'https://insights.glassnode.com/the-week-onchain-week-42-2022/',
            'https://insights.glassnode.com/the-week-onchain-week-32-2022/',
            'https://insights.glassnode.com/the-week-onchain-week-29-2022/',
            'https://insights.glassnode.com/the-week-onchain-week-33-2022/',
            'https://insights.glassnode.com/backtesting-in-workbench/',
            'https://insights.glassnode.com/the-week-onchain-week-37-2022/',
            'https://insights.glassnode.com/the-week-onchain-week-43-2022/',
            'https://insights.glassnode.com/defi-uncovered-experimental-lending-platforms/',
            'https://insights.glassnode.com/buying-the-dip-investors-accumulate/',
            'https://insights.glassnode.com/segwit-adoption/',
            'https://insights.glassnode.com/defi-uncovered-experiments-in-money-and-value/',
            'https://insights.glassnode.com/the-week-onchain-week-26-2022/',
            'https://insights.glassnode.com/defi-uncovered-exploring-the-sushi-ecosystem/',
            'https://insights.glassnode.com/the-week-onchain-week-27-2022/',
            'https://insights.glassnode.com/nfts-and-gaming-lead-the-eth-rally/',
            'https://insights.glassnode.com/sushi-vs-unicorn-the-rise-and-fall-of-uniswap/',
            'https://insights.glassnode.com/the-week-on-chain-week-29-2021/']

alert_ideas = []

for webpage in webpages:
    # Send a GET request to the webpage
    response = requests.get(webpage)

    # Decode the HTML content using UTF-8 encoding
    html_content = response.content.decode('utf-8')

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all paragraphs containing "Alert idea:"
    for paragraph in soup.find_all('p'):
        if 'alert idea:'.lower() in paragraph.text.lower():
            alert_idea_text = paragraph.text.strip()
            alert_idea_link = paragraph.find('a')['href']
            alert_ideas.append((alert_idea_text, alert_idea_link))

# Save the extracted alert ideas and their links to a CSV file
alert_ideas_df = pd.DataFrame(alert_ideas, columns=['content', 'link'])
alert_ideas_df.to_csv('alert_idea.csv', index=False)
