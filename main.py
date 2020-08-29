import os
from indeed import get_jobs_indeed
from so import get_jobs_so

os.system("clear")

dict_idx_sites = {
  0: ["indeed", get_jobs_indeed],
  1: ["stack overflow", get_jobs_so]
}

DESIRE_KEYWORD = "AI"
DESIRE_PAGES = None
SELECTED_SITES = [0, 1]

jobs = []

for site_idx in SELECTED_SITES:
  jobs += dict_idx_sites[site_idx][1](DESIRE_KEYWORD, DESIRE_PAGES)
#jobs_indeed = get_jobs_indeed(DESIRE_KEYWORD, DESIRE_PAGES)

for job in jobs:
  print(job,"\n")