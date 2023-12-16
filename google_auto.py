from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#taking input from the user
search_string = input("Input the URL or string you want to search on the browser:")


#structure the url into search url
search_string = search_string.replace(" ", "+")

#assigning the browser variable with chromedriver of Chrome
service = Service(executable_path="C:/Development/chromedriver.exe", log_path="NUL")
driver = webdriver.Chrome(service=service)


for i in range(1):
    matched_elements = driver.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))
