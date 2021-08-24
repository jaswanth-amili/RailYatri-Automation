"""
This module contains RailYatriResultPage,
the page object for the RailYatri search result page.
"""

from selenium.webdriver.common.by import By


class RailYatriResultPage:
  
  # Locators
  RESULT_FROM = (By.CSS_SELECTOR, 'p.Departure-time-text-2')
  RESULT_TO = (By.CSS_SELECTOR, 'p.Arrival-time-text-2')

  # Initializer
  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods
  def result_from_staion(self):
    from_stations = self.browser.find_elements(*self.RESULT_FROM)
    from_station = [link.text for link in from_stations]
    return from_station
  
  def result_to_staion(self):
    to_stations = self.browser.find_elements(*self.RESULT_TO)
    to_station = [link.text for link in to_stations]
    return to_station

  def title(self):
    return self.browser.title