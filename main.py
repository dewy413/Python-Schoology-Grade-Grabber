import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


i = input("How many courses are you taking? (You count a lab as a separate class) \n")

options = Options()
#options.add_argument("headless")
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

driver.get("https://lyon.schoology.com/grades/grades")

user = driver.find_element(By.ID, "userNameInput")
pss = driver.find_element(By.ID, "passwordInput")

username = input("Enter your username\n")
user.send_keys(username)
password = input("Enter your password\n")
pss.send_keys(password)

pss.submit()



for i in range(3, 9):
    clss = driver.find_element(By.XPATH,
                               "/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div[3]/div/div/div/div[{}]".format(
                                   i))
    try:
        grade = driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div[3]/div[1]/div[2]/div/div/div[3]/div/div/div/div[{}]/div[2]/table/tbody/tr[2]/td[1]/div/span/span/span".format(
                                        i))
        grade = grade.get_attribute('innerHTML')

    except selenium.common.exceptions.NoSuchElementException as final:
        grade = "N/A"

    print(f"{clss.text} - {grade}")

print("\nSCRIPT COMPLETE")

driver.close()