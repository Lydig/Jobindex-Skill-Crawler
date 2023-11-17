import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from collections import Counter

# Read job offer URLs from job_links.txt
with open('job_links.txt', 'r') as file:
    job_links = [line.strip() for line in file.readlines()]

# Initialize a list to store extracted words
extracted_words = []

# Define relevant IT skills (case-insensitive)
relevant_skills = [
    'python', 'java', 'sql', 'javascript', 'html', 'css', 'docker', 'aws', 
    'machine learning', 'data analysis', 'api', 'php', 'ruby', 'c++', 'c#', 
    'linux', 'unix', 'devops', 'git', 'web development', 'mobile app development', 
    'database management', 'networking', 'cloud computing', 'cybersecurity', 
    'agile', 'data science', 'big data', 'artificial intelligence', 'frontend', 
    'backend', 'full stack', 'software development', 'user experience (UX)', 
    'user interface (UI)', 'automation', 'testing', 'IoT', 'blockchain', 'VR/AR',
    'react', 'angular', 'node.js', 'typescript', 'swift', 'kotlin', 'scala', 
    'data engineering', 'ETL', 'data warehousing', 'cloud architecture', 'RESTful', 
    'GraphQL', 'microservices', 'CI/CD', 'containerization', 'scalability', 
    'virtualization', 'machine vision', 'natural language processing', 
    'serverless', 'cloud-native', 'edge computing', 'noSQL', 'R', 'MATLAB', 
    'Hadoop', 'Spark', 'Kubernetes', 'Jenkins', 'Ansible', 'Chef', 'Puppet', 
    'Splunk', 'ELK stack', 'Splunk', 'Apache', 'NGINX', 'Django', 'Flask', 
    'Spring', 'Ruby on Rails', 'Express.js', 'Vue.js', 'Ember.js', 'jQuery', 
    'Redux', 'Webpack', 'Gulp', 'Grunt', 'Sass', 'Less', 'Bootstrap', 
    'Material UI', 'Ant Design', 'UI/UX design', 'REST API', 'SOAP', 'GraphQL',
    'OAuth', 'JWT', 'OAuth2', 'Swagger', 'Postman', 'SOAP UI', 'TDD', 'BDD', 
    'Selenium', 'JIRA', 'Confluence', 'Agile methodologies', 'Scrum', 'Kanban', 
    'Waterfall', 'ITIL', 'COBOL', 'Mainframe', 'ERP systems', 'SAP', 
    'Salesforce', 'ServiceNow', 'Microsoft Office', 'Adobe Creative Cloud', 
    'Photoshop', 'Illustrator', 'InDesign', 'Premiere Pro', 'After Effects'
]

# Initialize a Selenium webdriver
driver = webdriver.Chrome()  # You'll need to download the Chrome WebDriver executable

# Iterate through each job offer URL
for job_link in job_links:
    driver.get(job_link)

    # Allow time for JavaScript content to load (you might need to adjust the sleep time)
    time.sleep(2)

    # Get the page source after JavaScript content has loaded
    page_source = driver.page_source

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page_source, 'html.parser')

    # Extract text from the entire page
    page_text = soup.get_text()

    # Use regular expressions to split text into words
    words = re.findall(r'\b\w+\b', page_text.lower())

    # Add words to the extracted_words list
    extracted_words.extend(words)

# Close the Selenium webdriver
driver.quit()

# Find relevant IT skills
extracted_skills = [word for word in extracted_words if word in relevant_skills]

# Print the extracted IT skills
print("Extracted IT Skills:")
print(extracted_skills)

# Assuming you have the extracted skills in the `extracted_skills` list
# Count the occurrences of each skill
skill_counts = Counter(extracted_skills)

# Sort the skills by frequency in descending order
sorted_skills = sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)

# Print the sorted skills with counts
for skill, count in sorted_skills:
    print(f"{skill}: {count}")