from playwright.sync_api import sync_playwright

def test_t2_login():
    """T2 QA Login Test - Real Work Environment"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        
        test_data = {
            "url": "https://dukeport201.t2qa.com/DUKEQA1/adm/users/auth.aspx?from=https://dukeport201.t2qa.com/DUKEQA1/adm/dev/impersonateUser.aspx",
            "username": "Kasey1",
            "password": "Parking123!!!",
            "expected_text": "Impersonate"
        }
        
        print("Starting T2 login test...")
        
        # Navigate to login page
        page.goto(test_data["url"])
        print("Navigated to login page")
        
        # Fill login form with correct selectors
        page.fill("#ctl00_T2Main_txtLogin", test_data["username"])
        page.fill("#ctl00_T2Main_txtPassword", test_data["password"])
        print("Entered credentials")
        
        # Click login button
        page.click("#ctl00_T2Main_cmdLogin")
        print("Clicked login button")
        
        # Wait for navigation and check if login worked
        page.wait_for_load_state("networkidle")
        
        if test_data["expected_text"] in page.content():
            print("LOGIN TEST: PASS")
        else:
            print("LOGIN TEST: FAIL")
            print(f"Current URL: {page.url}")
        
        input("Press Enter to close browser...")
        browser.close()

if __name__ == "__main__":
    test_t2_login()