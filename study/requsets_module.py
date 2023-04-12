# no standard libray. that's pypi user project.
from requests import get

websites = ("google.com", "airbnb.com", "https://twitter.com", "facebook.com",
            "https://tiktok.com")
result = {}
for website in websites:
  if not website.startswith("https://"):
    website = f"https://{website}"
  # computer commuication is HTTP request
  response = get(website)
  status = response.status_code
  if status >= 200:
    result[website] = "successfully"
  elif status >= 300:
    result[website] = "redirection"
  elif status >= 400:
    result[website] = "client error"
  elif status >= 500 and status < 600:
    result[website] = "server error"
  else:
    result[website] = "unknown error"

print(result)