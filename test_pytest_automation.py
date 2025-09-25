import pytest
from playwright.sync_api import sync_playwright

class TestT2Login:
    """PyTest class for FlexPort testing"""
    
    @pytest.fixture
    def browser_setup(self):
        """Setup browser for testing"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=500)
            page = browser.new_page()
            yield page
            browser.close()
    
    def test_valid_login(self, browser_setup):
        """Test valid login credentials"""
        page = browser_setup
        
        # Test data
        login_url = "https://dukeport201.t2qa.com/DUKEQA1/adm/users/auth.aspx?from=https://dukeport201.t2qa.com/DUKEQA1/adm/dev/impersonateUser.aspx"
        username = "Kasey1"
        password = "Parking123!!!"
        
        # Execute test
        page.goto(login_url)
        page.fill("#ctl00_T2Main_txtLogin", username)
        page.fill("#ctl00_T2Main_txtPassword", password)
        page.click("#ctl00_T2Main_cmdLogin")
        
        page.wait_for_load_state("networkidle")
        
        # Assertion
        assert "Impersonate" in page.content()
    
    def test_invalid_login_user(self, browser_setup):
        """Test invalid login credentials"""
        page = browser_setup
        
        login_url = "https://dukeport201.t2qa.com/DUKEQA1/adm/users/auth.aspx?from=https://dukeport201.t2qa.com/DUKEQA1/adm/dev/impersonateUser.aspx"
        
        # Execute test with invalid Username
        page.goto(login_url)
        page.fill("#ctl00_T2Main_txtLogin", "wronguser")
        page.fill("#ctl00_T2Main_txtPassword", "Parking123!!!")
        page.click("#ctl00_T2Main_cmdLogin")
        
        page.wait_for_load_state("networkidle")
        
        # Should stay on login page or show error
        assert "auth.aspx" in page.url
        
    def test_invalid_login_pw(self, browser_setup):
        """Test invalid login credentials"""
        page = browser_setup
        
        login_url = "https://dukeport201.t2qa.com/DUKEQA1/adm/users/auth.aspx?from=https://dukeport201.t2qa.com/DUKEQA1/adm/dev/impersonateUser.aspx"
        
        # Execute test with invalid Username
        page.goto(login_url)
        page.fill("#ctl00_T2Main_txtLogin", "Kasey1")
        page.fill("#ctl00_T2Main_txtPassword", "WrongPassword!")
        page.click("#ctl00_T2Main_cmdLogin")
        
        page.wait_for_load_state("networkidle")
        
        # Should stay on login page or show error
        assert "auth.aspx" in page.url 