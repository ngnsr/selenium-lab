from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_message_and_assert(driver, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.text_to_be_present_in_element(
                (By.ID, "message"), "Received!"
            )
        )
        message = driver.find_element(By.ID, "message").text
        assert "Received!" == message, f"Очікуваний текст 'Received!', але отримано: {message}"
        return True
    except TimeoutError:
        print("❌ Тест не пройшов: таймаут при очікуванні 'Received!'")
        return False
    except AssertionError as e:
        print(f"❌ Тест не пройшов: {str(e)}")
        return False


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    return webdriver.Chrome(options)

def test_text_input_and_submit():
    driver = setup_driver()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    text_input = driver.find_element(By.NAME, "my-text")
    text_input.send_keys("Hello, Selenium!")

    submit_btn = driver.find_element(By.TAG_NAME, "button")
    submit_btn.click()

    if wait_for_message_and_assert(driver):
        print("✅ Тест 1 пройдено")
    driver.quit()


def test_dropdown_and_submit():
    driver = setup_driver()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    dropdown = driver.find_element(By.NAME, "my-select")
    dropdown.find_element(By.XPATH, "./option[@value='2']").click()

    # Натискання кнопки
    submit_btn = driver.find_element(By.TAG_NAME, "button")
    submit_btn.click()

    if wait_for_message_and_assert(driver):
        print("✅ Тест 2 пройдено")
    driver.quit()


def test_checkbox_and_date_input():
    driver = setup_driver()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    checkbox = driver.find_element(By.NAME, "my-check")
    if not checkbox.is_selected():
        checkbox.click()

    date_input = driver.find_element(By.NAME, "my-date")
    date_input.send_keys("2025-04-14")

    submit_btn = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("arguments[0].click();", submit_btn)

    if wait_for_message_and_assert(driver):
        print("✅ Тест 3 пройдено")
    driver.quit()


if __name__ == "__main__":
    test_text_input_and_submit()
    test_dropdown_and_submit()
    test_checkbox_and_date_input()
