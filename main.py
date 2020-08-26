from indeed import get_jobs_indeed

dict_idx_sites = {
  0: ["indeed", get_jobs_indeed]
}

DESIRE_KEYWORD = "AI"
DESIRE_PAGES = 2
SELECTED_SITES = [0]

jobs = []

for site_idx in SELECTED_SITES:
  jobs += dict_idx_sites[site_idx][1](DESIRE_KEYWORD, DESIRE_PAGES)
#jobs_indeed = get_jobs_indeed(DESIRE_KEYWORD, DESIRE_PAGES)

print(jobs)