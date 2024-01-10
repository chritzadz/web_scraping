from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import keyboard
import time

#input
url_wos = "https://www.webofscience.com/wos/woscc/basic-search"


def launchBrowserWOS(search_query):
     start = 1
     stop = 500
     start_num = 2
     stop_num = 3


     driver = webdriver.Chrome()
     driver.get(url_wos)
     driver.maximize_window()
     
     # search_website = driver.find_element(By.XPATH, '//input[@name="search"]')
     # search_website.send_keys("web of science")
     # search_website.send_keys(Keys.RETURN)
     # time.sleep(1)

     # search_website = driver.find_element(By.XPATH, '//a[@href="//lbsystem.lib.cityu.edu.hk/ereslist/details.php?id=631"]')
     # search_website.click()
     # time.sleep(1)

     # search_website_1 = driver.find_element(By.XPATH, '//a[@href="http://libweb.cityu.edu.hk/cgi-bin/er/db/isiwebdb.pl"]')
     # search_website_1.click()
     # time.sleep(4)

     time.sleep(5)
     acc_all = driver.find_element("id", "onetrust-accept-btn-handler")
     acc_all.click()
     time.sleep(2)

     advanced_search_btn = driver.find_element(By.XPATH, '//a[@title="Use Advanced Search to Narrow Your Search to Specific Criteria"]')
     advanced_search_btn.click()
     time.sleep(2)

     search_query_text_area = driver.find_element("id", "advancedSearchInputArea")
     search_query_text_area.send_keys(search_query)
     
     search_query_advance_search_btn = driver.find_element(By.XPATH, '//button[@class="mat-focus-indicator search mat-flat-button mat-button-base mat-primary ng-star-inserted"]')
     search_query_advance_search_btn.click()
     time.sleep(2)

     paper_count_html = driver.find_element(By.XPATH, '//span[@class="brand-blue"]')
     total_paper = paper_count_html.get_attribute('innerHTML')
     time.sleep(3)

     #exporting
     while start < int(total_paper.replace(",", "")):
          export_btn = driver.find_element(By.XPATH, '//button[@class="mat-focus-indicator mat-menu-trigger margin-right-10--reversible mat-stroked-button mat-button-base mat-primary"]')
          export_btn.click()
          time.sleep(2)

          export_method_btn = driver.find_element('id', "exportToTabWinButton")
          export_method_btn.click()
          time.sleep(2)

          record_content_btn = driver.find_element(By.XPATH, '//button[@class="dropdown"]')
          record_content_btn.click()
          time.sleep(2)

          record_content_selection = driver.find_element(By.XPATH, '//div[@title="Full Record and Cited References"]')
          record_content_selection.click()
          time.sleep(3)

          records_from_radio_btn = driver.find_element(By.ID, 'radio3-input')

          if records_from_radio_btn.is_selected():
               pass
          else:
               driver.execute_script("arguments[0].click();", records_from_radio_btn)

          time.sleep(3)

          start_input_area = driver.find_element("id", 'mat-input-' + str(start_num))
          start_input_area.clear()
          start_input_area.send_keys(str(start))
          time.sleep(2)

          stop_input_area = driver.find_element("id", 'mat-input-' + str(stop_num))
          stop_input_area.clear()
          stop_input_area.send_keys(str(stop))
          time.sleep(2)

          export_final_btn = driver.find_element(By.XPATH, '//button[@class="mat-focus-indicator mat-flat-button mat-button-base mat-primary"]')
          export_final_btn.click()
          time.sleep(10)

          start += 500
          stop += 500
          start_num += 2
          stop_num += 2

          print(total_paper)
          print(start)
