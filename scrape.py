# from selenium.webdriver import Remote, ChromeOptions
# from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
# from bs4 import BeautifulSoup
# from dotenv import load_dotenv
# import os

# load_dotenv()

# SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")


# def scrape_website(website):
#     print("Connecting to Scraping Browser...")
#     sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
#     with Remote(sbr_connection, options=ChromeOptions()) as driver:
#         driver.get(website)
#         print("Waiting captcha to solve...")
#         solve_res = driver.execute(
#             "executeCdpCommand",
#             {
#                 "cmd": "Captcha.waitForSolve",
#                 "params": {"detectTimeout": 10000},
#             },
#         )
#         print("Captcha solve status:", solve_res["value"]["status"])
#         print("Navigated! Scraping page content...")
#         html = driver.page_source
#         return html


# def extract_body_content(html_content):
#     soup = BeautifulSoup(html_content, "html.parser")
#     body_content = soup.body
#     if body_content:
#         return str(body_content)
#     return ""


# def clean_body_content(body_content):
#     soup = BeautifulSoup(body_content, "html.parser")

#     for script_or_style in soup(["script", "style"]):
#         script_or_style.extract()

#     # Get text or further process the content
#     cleaned_content = soup.get_text(separator="\n")
#     cleaned_content = "\n".join(
#         line.strip() for line in cleaned_content.splitlines() if line.strip()
#     )

#     return cleaned_content


# def split_dom_content(dom_content, max_length=6000):
#     return [
#         dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
#     ]



from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Ensure SBR_WEBDRIVER is correctly retrieved
SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")
if not SBR_WEBDRIVER:
    raise ValueError("SBR_WEBDRIVER environment variable is not set or is empty.")

def scrape_website(website):
    """Scrapes a website by connecting through the specified Scraping Browser Remote (SBR)."""
    print("Connecting to Scraping Browser...")
    try:
        # Establish a connection with the Scraping Browser Remote
        sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
        with Remote(sbr_connection, options=ChromeOptions()) as driver:
            # Navigate to the website
            driver.get(website)
            print("Waiting for CAPTCHA to be solved...")
            
            # Example CAPTCHA handling (might need adjustments based on SBR capabilities)
            solve_res = driver.execute(
                "executeCdpCommand",
                {
                    "cmd": "Captcha.waitForSolve",
                    "params": {"detectTimeout": 10000},
                },
            )
            
            # Log CAPTCHA solve status
            captcha_status = solve_res.get("value", {}).get("status", "unknown")
            print("CAPTCHA solve status:", captcha_status)
            
            # Scrape page content after CAPTCHA is solved
            print("Navigated! Scraping page content...")
            html = driver.page_source
            return html
    except Exception as e:
        print(f"An error occurred while scraping: {e}")
        return None

def extract_body_content(html_content):
    """Extracts the <body> content from the HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    """Cleans the body content by removing <script>, <style>, and unwanted elements."""
    soup = BeautifulSoup(body_content, "html.parser")

    # Remove all <script> and <style> tags
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Extract and clean text content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    """Splits the DOM content into chunks of a specified maximum length."""
    return [
        dom_content[i : i + max_length]
        for i in range(0, len(dom_content), max_length)
    ]
