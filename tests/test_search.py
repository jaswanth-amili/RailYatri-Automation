"""
These tests cover RailYatri searches.
"""
import time
from pages.result import RailYatriResultPage
from pages.search import RailYatriSearchPage


def test_basic_RailYatri_search(browser):
  search_page = RailYatriSearchPage(browser)
  result_page = RailYatriResultPage(browser)
  PHRASE = "RailYatri"
  from_code = "NDLS"
  to_code = "HYB"
  from_station="delhi"
  to_station="hyderabad"

  
  # Given the RailYatri train ticket page is displayed
  search_page.load()
  time.sleep(1)
  # When user searches from as "Delhi" and to as "Hyderabad" and click on Search Trains
  search_page.search(from_code,to_code)

  # Then the search result query is "panda"
  # assert PHRASE == result_page.search_input_value()
  
  # And the search result links pertain to "Delhi -> Hyderabad"
  from_titles = result_page.result_from_staion()
  from_matches = [f for f in from_titles if from_station.lower() in f.lower()]
  assert len(from_matches) > 0

  to_titles = result_page.result_to_staion()
  to_matches = [t for t in to_titles if to_station.lower() in t.lower()]
  assert len(to_matches) > 0

  # And verify the content of the page
  assert PHRASE in result_page.title()

  
  