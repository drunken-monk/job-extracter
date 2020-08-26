from indeed import get_jobs_indeed

DESIRE_KEYWORD = "javascript"
DESIRE_PAGES = 2

jobs_indeed = get_jobs_indeed(DESIRE_KEYWORD, DESIRE_PAGES)
print(jobs_indeed)