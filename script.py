from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
# # edgedriver_path = 'C:/Users/cdagg/OneDrive - Blackrock College/Documents/Edgewinner/msedgedriver.exe'
# edgedriver_path = '/Users/nialldagg/msedgedriver.exe'
driver = webdriver.Edge()
driver.get("https://liftingcast.com/meets/mhla55j0xvxt/results")
csv_file = open("liftingcast_results.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "Team", "Place", "BW", "SQ1", "SQ2", "SQ3", "BP1", "BP2", "BP3", "ST", "DL1", "DL2", "DL3", "DOTS/TOTAL"])

#THIS IS THE SLECTOR FOR EACH ROW
starting_selector = "//*[@id='app']/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div["
ending_selector = "]/div"


#THIS IS THE SLECTOR FOR EACH NAME
starting_name = "//*[@id='app']/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div["
ending_name = "]/div/a"
data_values = []
name_list = [4, 7, 16] 

#THIS IS TO ADD EACH NAME TO THE CSV FILE
for i in range(len(name_list)):
    name_elements = driver.find_element(By.XPATH, starting_name + str(name_list[i]) + ending_name)
    print(name_elements.text)
    csv_writer.writerow([name_elements.text])

#THIS IS TO ADD EACH ROW TO THE CSV FILE
for i in range(12, 33):
    
    elements = driver.find_element(By.XPATH, starting_selector + str(i) + ending_selector)
    data_values.append(elements.text)
   

for i in range(len(data_values)):
    print(data_values[i])
    csv_writer.writerow([data_values[i]])
