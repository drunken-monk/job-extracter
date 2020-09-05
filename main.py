import os
from indeed import get_jobs_indeed
from so import get_jobs_so
from wwr import get_jobs_wwr
import requests
from bs4 import BeautifulSoup

os.system("clear")

dict_idx_sites = {
  0: ["stack overflow", get_jobs_so],
  1: ["wwr", get_jobs_wwr],
  2: ["stack overflow", get_jobs_so],
  3: ["indeed", get_jobs_indeed],
}

DESIRE_KEYWORD = "python"
DESIRE_PAGES = None
SELECTED_SITES = [1]

jobs = []


for site_idx in SELECTED_SITES:
  jobs += dict_idx_sites[site_idx][1](DESIRE_KEYWORD, DESIRE_PAGES)

for job in jobs:
  print(job,"\n")

'''
keyword = "python"
url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}&utf8=%E2%9C%93"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
contents = soup.find("div", {"id": "job_list"})
items = contents.find_all("li")

for item in items:
  SITE_NAME = "weworkremotely"
  title = item.find("span", {"class": "title"})
  if title == None:
    continue
  title = item.find("span", {"class": "title"}).get_text(strip=True)
  company = item.find("span", {"class": "company"}).get_text(strip=True)
  try:
    company_anchor = item.select_one("li > a")["href"]
    company_anchor = f"https://weworkremotely.com{company_anchor}"
  except:
    company_anchor = "No Link"
  try:
    location = item.find("span", {"class": "region company"}).get_text(strip=True)
  except:
    location = "Anywhere"
  
  salary = "not opened"
  
  print(company_anchor)

'''
