from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # browser = p.chromium.launch(headless= False, slow_mo= 100000)
    dir_path = r"C:\Users\varad\AppData\Local\Google\Chrome\User Data\Profile 1"
    print("path :", dir_path)
    browser = p.chromium.launch_persistent_context(channel="chrome", slow_mo= 100000, user_data_dir= dir_path, headless=False)
    page = browser.new_page()
    page.goto("https://www.example.com/login")