import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv
import datetime

# funkcja tworząca nazwę pliku do zrzutu ekranowego
def make_screenshot(maps):
    now = datetime.datetime.now()
    screenshot = 'maps'+now.strftime('%H%M%S')+'.png'
    maps.get_screenshot_as_file(screenshot)

class GoogleMaps(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # otwiera stronę główną
        self.driver.get('https://www.google.com/maps/@51.134464,16.9621174,14z')
        # akceptacja plików cookie
        cookie_accept = self.driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button')
        cookie_accept.click()
        sleep(3)

    def tearDown(self):
        # Wyłącza przeglądarkę
        self.driver.quit()

    def test_coords_row_3(self):
        # otwiera plik .csv
        file = open('C:\\dane_csv\\dane_gps.csv')
        # zmienna "data" - czyta plik po wierszach
        self.data = [row for row in csv.reader(file)]
        # do zmiennej "data" przypisano konkretny wiersz dla potrzeb testu
        self.data = self.data[3]
        search_field = self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
        search_field.click()
        # w pole "szukaj" wprowadzone zostaję współrzędne wykonania fotografii
        search_field.send_keys(self.data)
        search_button = self.driver.find_element(By.ID, 'searchbox-searchbutton')
        search_button.click()
        sleep(5)
        # wykonanie zrzutu ekranu - potwierdzające działanie programu
        make_screenshot(self.driver)
        file.close()

    def test_coords_row_8(self):
        # otwiera plik .csv
        file = open('C:\\dane_csv\\dane_gps.csv')
        # zmienna "data" - czyta plik po wierszach
        self.data = [row for row in csv.reader(file)]
        # do zmiennej "data" przypisano konkretny wiersz dla potrzeb testu
        self.data = self.data[8]
        search_field = self.driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
        search_field.click()
        # w pole "szukaj" wprowadzone zostaje współrzędne wykonania fotografii
        search_field.send_keys(self.data)
        search_button = self.driver.find_element(By.ID, 'searchbox-searchbutton')
        search_button.click()
        sleep(5)
        # wykonanie zrzutu ekranu - potwierdzające działanie programu
        make_screenshot(self.driver)
        file.close()






