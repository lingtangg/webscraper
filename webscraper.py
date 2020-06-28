import requests
from bs4 import BeautifulSoup

# Get the html from the webpage
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

# Get the specific section of the html with job postings
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='SearchResults')

# Gets only the job details from the section
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(f'{title_elem.text.strip()}\n{company_elem.text.strip()}\n{location_elem.text.strip()}\n')

# Parse for a term
key_word = input('What type of job are you looking for? ')
python_jobs = results.findAll('h2', string=lambda text: key_word.lower() in text.lower())
for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(f'{p_job.text.strip()}')
    print(f'Apply here: {link}')