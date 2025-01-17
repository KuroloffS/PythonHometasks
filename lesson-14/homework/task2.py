import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

DB_FILE = "jobs.db"
JOBS_URL = "https://realpython.github.io/fake-jobs"

# Create database connection
def create_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        company TEXT,
                        location TEXT,
                        description TEXT,
                        apply_link TEXT,
                        UNIQUE(title, company, location)
                    )''')
    conn.commit()
    conn.close()

# Scrape job listings
def scrape_jobs():
    response = requests.get(JOBS_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    job_listings = []
    
    for job_card in soup.find_all("div", class_="card-content"):
        title = job_card.find("h2", class_="title").get_text(strip=True)
        company = job_card.find("h3", class_="company").get_text(strip=True)
        location = job_card.find("p", class_="location").get_text(strip=True)
        description = job_card.find("div", class_="description")
        description_text = description.get_text(strip=True) if description else "No description available"
        apply_link = job_card.find("a", string="Apply")
        apply_url = apply_link["href"] if apply_link else "No link available"

        job_listings.append((title, company, location, description_text, apply_url))
    
    return job_listings


# Store jobs in SQLite with incremental loading
def store_jobs(job_listings):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    for job in job_listings:
        cursor.execute('''INSERT INTO jobs (title, company, location, description, apply_link)
                          VALUES (?, ?, ?, ?, ?)
                          ON CONFLICT(title, company, location) DO UPDATE 
                          SET description=excluded.description, apply_link=excluded.apply_link''', job)
    
    conn.commit()
    conn.close()

# Filter jobs by location or company
def filter_jobs(location=None, company=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    query = "SELECT title, company, location, description, apply_link FROM jobs WHERE 1=1"
    params = []
    
    if location:
        query += " AND location=?"
        params.append(location)
    if company:
        query += " AND company=?"
        params.append(company)
    
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    
    return results

# Export filtered results to CSV
def export_to_csv(results, filename="filtered_jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location", "Description", "Application Link"])
        writer.writerows(results)
    print(f"Exported to {filename}")

# Run the script
if __name__ == "__main__":
    create_db()
    jobs = scrape_jobs()
    store_jobs(jobs)
    print("Job listings updated.")
