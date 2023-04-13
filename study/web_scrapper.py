from requests import get
from bs4 import BeautifulSoup


def extract_paiza_jobs(keyword, page):
  base_url = "https://paiza.jp/student/job_offers/dev_language/"
  response = get(f"{base_url}{keyword}?page={page}")
  if response.status_code != 200:
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
      job_data = {'company': company.string, 'work': work.string, 'link': link}
      results.append(job_data)
    for result in results:
      print(result)
      print()


lang = input("What programming language? ")
page = int(input("What page do you want to print? "))
extract_paiza_jobs(lang, page)
