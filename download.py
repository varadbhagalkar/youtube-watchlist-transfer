from playwright.sync_api import sync_playwright
from random import randint
from time import sleep
import my_data as mydata
with sync_playwright() as p:
	browser = p.chromium.launch(**{
		'args': ["--disable-blink-features=AutomationControlled"],
		'headless': False,
		'channel':'chrome'
	})
	context1=browser.new_context()
	page1 = context1.new_page()
	page1.goto('https://www.youtube.com')
	sleep(randint(3,15))
	page1.get_by_label("Sign in").click()
	sleep(randint(3,15))
	page1.get_by_role("textbox").fill(mydata.USERNAME)
	sleep(randint(3,15))
	page1.get_by_role("button",name="Next").click()
	sleep(randint(3,15))
	page1.get_by_role("textbox").fill(mydata.PASSWORD)
	sleep(randint(3,15))
	page1.get_by_role("button",name="Next").click()
	
	sleep(100)

	page2=context1.new_page()
	page2.goto("https://www.youtube.com/watch?v=ckpotxktdvY")
	sleep(1000)

	# page1.wait_for_timeout(10000)
	# i=input("Do you want to proceed?: ")
	# page1.get_by_role("textbox", name="Search").click()
	# page1.get_by_role("textbox", name="Search").fill("Cal Newport")
	# page1.get_by_label("Search").click()
	

	# context2=browser.new_context()
	# page2=context2.new_page()
	# page2.goto('https://www.youtube.com')
	# page2.get_by_alt_text("Search")
	# page1.pause()

	
	# page.get_by_role("textbox", name="Search").click()
	# page.get_by_role("textbox", name="Search").fill("Coding")
	# page.wait_for_timeout(10000)
	# page.get_by_role("", name="Search").click()
	# page.get_by_label("Sign in").click()
	# page.get_by_role("textbox").fill(mydata.USERNAME)
	# page.get_by_role("button",name="Next").click()
	# lc=page.locator("Sign in")
	# lc.click()
	# page.wait_for_timeout(10000)
	# browser.close()