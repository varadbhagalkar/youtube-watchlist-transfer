from playwright.sync_api import sync_playwright
import my_data as mydata
with sync_playwright() as p:
	browser = p.chromium.launch(headless=False)
	context=browser.new_context()
	page = context.new_page()
	page.goto('https://www.youtube.com')
	# page.get_by_role("textbox", name="Search").click()
	# page.get_by_role("textbox", name="Search").fill("Coding")
	# page.wait_for_timeout(10000)
	# page.get_by_role("", name="Search").click()
	page.get_by_label("Sign in").click()
	page.get_by_role("textbox").fill(mydata.USERNAME)
	# lc=page.locator("Sign in")
	# lc.click()
	page.wait_for_timeout(10000)
	# browser.close()