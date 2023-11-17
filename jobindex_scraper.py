#.\venv\Scripts\activate
from bs4 import BeautifulSoup
import requests

# Define the base URL and headers
base_url = 'https://www.jobindex.dk/jobsoegning?geoareaid=2&geoareaid=1221'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

# Create an empty list to store the href links
href_links = []

# Iterate through 10 pages
for page_number in range(1, 47):  # Adjust the range for the number of pages you want to scrape
    # Modify the URL to include the page number
    url = f'{base_url}&page={page_number}&q=programmer+it+programm%C3%B8r&subid=1&subid=2&subid=3&subid=4&subid=6&subid=7&subid=93'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <div class="PaidJob"> elements
        paid_job_elements = soup.find_all('div', class_='PaidJob')

        # Extract the href from the h4 a element within each PaidJob element
        for paid_job in paid_job_elements:
            h4_a = paid_job.find('h4').find('a')
            if h4_a:
                href = h4_a.get('href')
                href_links.append(href)
                print(f"Found PaidJob with href: {href}")

        print(f"Scraped page {page_number}")
    else:
        print(f"Failed to retrieve page {page_number}. Status code: {response.status_code}")

# Save the href links to a text file
with open('job_links.txt', 'w') as file:
    for link in href_links:
        file.write(link + '\n')

print(f"Saved {len(href_links)} job links to job_links.txt")
