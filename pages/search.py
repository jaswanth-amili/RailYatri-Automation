"""
This module contains RailYatriSearchPage,
the page object for the RailYatri search page.
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class RailYatriSearchPage:

  # URL
  URL = 'https://www.railyatri.in/train-ticket'

  # Locators
  FROM_STATION = (By.XPATH, '//input[@id="boarding_from"]')
  TO_STATION = (By.XPATH, '//input[@id="boarding_to"]')
  SEARCH_BUTTON = (By.XPATH, '//button[@id="tt_search_dweb"]')

  # Initializer
  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods
  def load(self):
    self.browser.get(self.URL)

  def search(self, from_station, to_station):
    from_element = self.browser.find_element(*self.FROM_STATION)
    to_element = self.browser.find_element(*self.TO_STATION)
    button_element = self.browser.find_element(*self.SEARCH_BUTTON)
    from_element.click()
    from_element.send_keys(from_station)
    time.sleep(1.5)
    from_element.send_keys(Keys.DOWN)
    from_element.send_keys(Keys.RETURN)

    to_element.click()
    to_element.send_keys(to_station)
    time.sleep(1.5)
    to_element.send_keys(Keys.DOWN)
    to_element.send_keys(Keys.RETURN)
    button_element.click()
