import requests
from bs4 import BeautifulSoup

LIMIT = 50
DESIRE_KEYWORD = "python"
URL = ""


def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class": "pagination"})
  pages = pagination.find_all("a")
  spans = []
  for page in pages[:-1]:
      spans.append(int(page.string))
  max_page = max(spans)

  return max_page


def extract_jobs_indeed(html):
  title = html.find("h2", {"class": "title"})
  title = title.find("a")["title"]
  company = html.find("span", {"class": "company"})
  company_anchor = company.find("a")
  if company_anchor is not None:
      company = str(company_anchor.string)
  else:
      company = str(company.string)
  company = company.strip()
  location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
  salary = html.find("span", {"class": "salaryText"})
  salary = salary.string if salary is not None else "not opened"
  job_id = html["data-jk"]

  return {
    "title": title,
    "company": company,
    "location": location,
    "salary": salary,
    "link": f"https://www.indeed.com/viewjob?jk={job_id}"
  }


def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"==============={page+1}page===============")

    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

    for result in results:
      jobs.append(extract_jobs_indeed(result))
  

  return jobs

def get_jobs_indeed(desire_keyword, desire_pages = None):
  global DESIRE_KEYWORD, URL
  DESIRE_KEYWORD = desire_keyword
  URL = f"https://www.indeed.com/jobs?as_and={DESIRE_KEYWORD}&sort=&limit={LIMIT}"
  print(URL)
  last_page = extract_indeed_pages()
  last_page = last_page if desire_pages is None else desire_pages
  jobs = extract_indeed_jobs(last_page)
  return jobs