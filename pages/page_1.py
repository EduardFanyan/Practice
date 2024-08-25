import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base_.base_1 import Base


class RandomTest(Base):
    url = r'https://randstuff.ru/number/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    number_start = '//input[@id="number-start"]'
    number_end = '//input[@id="number-end"]'
    button_gen = '//button[@id="button"]'
    number_save = '//div[@id="number-save"]'
    save_link = '//a[@class="save-link"]'
    button_clo = ('//button[@class="ui-button ui-widget ui-state-default ui-corner-all '
                  'ui-button-icon-only ui-dialog-titlebar-close"]')

    # Методы

    def get_number_start(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_start)))

    def get_number_end(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_end)))

    def get_button_gen(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_gen)))

    def get_result_gen1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_save)))

    def get_result_gen2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.save_link)))

    def get_result_gen3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_clo)))

    # Действия

    def number_start_text(self, input_number_s):
        self.get_number_start().send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.get_number_start().send_keys(input_number_s)
        print(f'Вводим стартовое значение: {input_number_s}')

    def number_end_text(self, input_number_e):
        self.get_number_end().send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        self.get_number_end().send_keys(input_number_e)
        print(f'Вводим финишное значение: {input_number_e}')

    def click_button(self):
        self.get_button_gen().click()
        print('Жмем сгенерировать')

    def click_button_get_result_gen(self):
        time.sleep(2)
        self.get_result_gen1().click()
        time.sleep(3)
        print('Жмем сохранить результат, переходим на вкладку, где можно проверить результат, нормально')
        self.get_result_gen2().click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        self.get_result_gen3().click()

    # Тесты

    def random_test_1(self):
        self.driver.get(self.url)
        self.number_start_text('1')
        self.number_end_text('100')
        self.click_button()
        self.click_button_get_result_gen()
        result1 = self.driver.find_element(By.XPATH, '//span[@class="cur"]').text
        assert 1 <= int(result1) <= 100, 'Результат не допустим'
        print(f'Результат допустим: {result1}')
        self.driver.close()

    def random_test_2(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.refresh()
        self.number_start_text('1')
        self.number_end_text('1')
        self.click_button()
        self.click_button_get_result_gen()
        result2 = self.driver.find_element(By.XPATH, '//span[@class="cur"]').text
        assert int(result2) == 1, 'Результат не допустим'
        print(f'Результат допустим: {result2}')
        time.sleep(2)
        self.driver.close()

    def random_test_3(self):
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.refresh()
        self.number_start_text('23')
        self.number_end_text('13')
        self.click_button()
        self.click_button_get_result_gen()
        result3 = self.driver.find_element(By.XPATH, '//span[@class="cur"]').text
        assert 13 <= int(result3) <= 23, 'Результат не допустим'
        print(f'Результат допустим: {result3}')
        self.driver.close()
