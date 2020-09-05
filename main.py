import os
from indeed import get_jobs_indeed
from so import get_jobs_so
from wwr import get_jobs_wwr
from remoteok import get_jobs_remoteok

import requests
from bs4 import BeautifulSoup

os.system("clear")

dict_idx_sites = {
  0: ["stack overflow", get_jobs_so],
  1: ["wwr", get_jobs_wwr],
  2: ["remoteok", get_jobs_remoteok],
  3: ["indeed", get_jobs_indeed],
}

DESIRE_KEYWORD = "python"
DESIRE_PAGES = None
SELECTED_SITES = [2]

jobs = []


for site_idx in SELECTED_SITES:
  jobs += dict_idx_sites[site_idx][1](DESIRE_KEYWORD, DESIRE_PAGES)

for job in jobs:
  print(job,"\n")


'''
keyword = "python"
url = f"https://remoteok.io/remote-{keyword}-jobs"

result = requests.get(url)

soup = BeautifulSoup(result.text, "html.parser")
contents = soup.find("table", {"id": "jobsboard"})
items = contents.find_all("tr", {"class": "job"})

for item in items:

  SITE_NAME = "remoteok"
  id = item["data-id"]
  item = item.find("td", {"class": "company position company_and_position_mobile"})
  if id == None:
    continue
  #print(id)
  title = item.find("h2").get_text(strip=True)
  company = item.find("h3").get_text(strip=True)
  try:
    company_anchor = f"https://remoteok.io/l/{id}"
  except:
    company_anchor = "No Link"
  try:
    location = item.find("span", {"class": "location"}).get_text(strip=True)
    print(location)
  except:
    location = "Anywhere"
    print(location)
  
  salary = "not opened"
  
  #print(company_anchor)
  
'''