from requests import get
from bs4 import BeautifulSoup


def extract_paiza_jobs(keyword, page):
  base_url = "https://paiza.jp/student/job_offers/dev_language/"

  response = get(f"{base_url}{keyword}?page={page}")
  if response.status_code != 200:
    if response.status_code == 404:
      return False
    else:
      print(f"Can't request website error is {response.status_code}")
  else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("div", class_="c-job_offer-box")
    results = []
    for job in jobs:
      companys = job.find("h4", class_="c-job_offer-recruiter__name")
      company = companys.find("a")
      work = job.find("div", class_="c-job_offer-detail__occupation")
      link = f"https://paiza.jp{company['href']}"
      job_data = {
        'company': company.string.replace(",", " "),
        'work': work.string.replace(",", " "),
        'link': link.replace(",", " ")
      }
      results.append(job_data)
  return results
