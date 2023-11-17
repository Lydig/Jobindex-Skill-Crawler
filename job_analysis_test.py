import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Example job offer URLs
job_links = [
    'https://evida.career.emply.com/ad/data-engineer/t78egu/da',
    # Add more job offer URLs here
]

# Initialize a list to store extracted words
extracted_words = []

# Define relevant IT skills (case-insensitive)
relevant_skills = ['python', 'java', 'sql', 'javascript', 'html', 'css', 'docker', 'aws', 'machine learning', 'data analysis', 'datafundament', 'windows', 'office', 'co2', 'engineer', 'modellering']

# Initialize a Selenium webdriver
driver = webdriver.Chrome()  # You'll need to download the Chrome WebDriver executable

# Iterate through each job offer URL
for job_link in job_links:
    driver.get(job_link)
    
    # Allow time for JavaScript content to load (you might need to adjust the sleep time)
    time.sleep(5)
    
    # Get the page source after JavaScript content has loaded
    page_source = driver.page_source
    
    # Create a BeautifulSoup object
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract text from the entire page
    page_text = soup.get_text()

    # Split the text into words and convert them to lowercase
    words = [word.lower() for word in page_text.split()]

    # Add words to the extracted_words list
    extracted_words.extend(words)

# Close the Selenium webdriver
driver.quit()

# Find relevant IT skills
extracted_skills = [word for word in extracted_words if word in relevant_skills]

# Print the extracted IT skills
print("Extracted IT Skills:")
print(extracted_skills)
