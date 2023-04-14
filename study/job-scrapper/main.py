from flask import Flask, render_template, request, redirect
from extractors.paiza import extract_paiza_jobs


# app name
app = Flask("JobScrapper")

# save cache
db = {}


# decorator
# Function to return when address is accessed
@app.route("/")
def home():
  return render_template("home.html", name="jun")


@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  page = request.args.get("page")
  if keyword == "":
    return redirect("/")
  if page == "":
    return redirect("/")
  else:
    page = int(request.args.get("page"))
  # Speed up once retrieved information by extracting values from cache divisors without running functions
  if (keyword and page) in db:
    jobs = db[keyword]
    page = db[page]
  else:
    jobs = extract_paiza_jobs(keyword, page)
    if jobs == False:
      error_message = "The keyword may not have a job or a page."
      return render_template("error.html", error_message=error_message)
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, page=page, jobs=jobs)


app.run("0.0.0.0")
