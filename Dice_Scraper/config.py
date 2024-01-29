# config.py
# config.py
class Config:
    API_KEY = "1YAt0R9wBg4WfsF9VB2778F5CHLAPMVW3WAZcKd8"
    HEADERS = {
        "authority": "job-search-api.svc.dhigroupinc.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "x-api-key": API_KEY,
    }
    CSV_FILENAME = "output.csv"
    SEARCH_TYPE = "1"
    KEYWORDS = ["Data Analyst", "Business Analyst", "System Analyst", "Data Scientists", "Data engineer", "Business System Analyst"]
    URL = "https://job-search-api.svc.dhigroupinc.com/v1/dice/jobs/search"

