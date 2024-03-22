from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from time import sleep
from PIL import Image
import captcha
import base64
import database

def run(email, password, country):
    # URL for login and registration
    url = "https://keliauk.urm.lt/en/consult_registration"

    # Loading the browser
    driver = webdriver.Chrome()
    driver.maximize_window() 
    driver.get(url)
    sleep(5)

    # Bypassing cloudflare
    iframes = driver.find_element(By.CSS_SELECTOR, "iframe[title=\"Widget containing a Cloudflare security challenge\"]")
    iframe_document = iframes.content_document
    pointer = driver.current_pointer
    pointer.move_to(500, 200, smooth_soft=60, total_time=0.5)
    pointer.move_to(20, 50, smooth_soft=60, total_time=0.5)
    pointer.move_to(8, 45, smooth_soft=60, total_time=0.5)
    pointer.move_to(500, 200, smooth_soft=60, total_time=0.5)
    pointer.move_to(166, 206, smooth_soft=60, total_time=0.5)
    pointer.move_to(200, 205, smooth_soft=60, total_time=0.5)
    iframe_document.find_element(By.CSS_SELECTOR, "input[type=\"checkbox\"]").click(move_to=True)

    # Automatically pressing cookie button 
    try:
        cookie_button = driver.find_element(By.ID, "bf1f70e3eae8f503623659673d5dca1e9")
        driver.execute_script("arguments[0].click();", cookie_button)
    except:
        sleep(3)
        try:
            cookie_button = driver.find_element(By.ID, "bf1f70e3eae8f503623659673d5dca1e9")
            driver.execute_script("arguments[0].click();", cookie_button)
        except:
            pass
    sleep(1)

    # Automatically pressing login button 
    try:
        login_button_parent = driver.find_element(By.CSS_SELECTOR, "button[class=\"btn outline-primary rounded-pill d-block d-lg-inline-block mb-3 px-4 btn-rounded-pill btn-depressed xlistener\"]")
        login_button = login_button_parent.find_element(By.CSS_SELECTOR, "span[class=\"btn-label\"]")
        login_button.click()
    except:
        sleep(3)
        try:
            login_button_parent = driver.find_element(By.CSS_SELECTOR, "button[class=\"btn outline-primary rounded-pill d-block d-lg-inline-block mb-3 px-4 btn-rounded-pill btn-depressed xlistener\"]")
            login_button = login_button_parent.find_element(By.CSS_SELECTOR, "span[class=\"btn-label\"]")
            login_button.click()
        except:
            pass
    sleep(4)

    # Function that converts image to base64
    def image_to_base64(image_path):
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()
            base64_data = base64.b64encode(image_bytes).decode("utf-8")
        return base64_data

    # Automatically input email and password
    email_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder=\"info@pastas.lt\"]")
    email_input.write(email)

    pwd_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"password\"]")
    pwd_input.write(password)

    # Generate captchaText
    captcha_input = driver.find_element(By.CSS_SELECTOR, "input[name=\"captcha\"]")
    captcha_img = driver.find_element(By.CSS_SELECTOR, "img[id=\"captcha_img\"]")
    driver.save_screenshot('captchaImage.png')
    location = captcha_img.location
    size = captcha_img.size
    driver.save_screenshot('screenshot.png') # Capture the screenshot of the element

    # Crop the screenshot to the element's dimensions
    left = int(location['x'])
    top = int(location['y'])
    right = int(location['x'] + size['width'])
    bottom = int(location['y'] + size['height'])

    screenshot = Image.open('screenshot.png')
    element_screenshot = screenshot.crop((left, top, right, bottom))
    element_screenshot.save('element_screenshot.png')
    image_path = "element_screenshot.png"
    base64_data = image_to_base64(image_path)
    captcha_text = captcha.solver_captcha(base64_data)
    captcha_input.write(captcha_text)

    # Submit credential 
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"btn primary px-5 rounded-pill btn-success btn-rounded-pill btn-depressed xlistener\"]")
    submit_button.click()
    sleep(5)

    # Error handling when failed login with wrong captcha
    try:
        error_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"btn btn-primary btn-rounded-pill btn-depressed\"]")
        error_button.click()
        sleep(2)
        captcha_img = driver.find_element(By.CSS_SELECTOR, "img[id=\"captcha_img\"]")
        captcha_img.click()
        sleep(2)
        captcha_img = driver.find_element(By.CSS_SELECTOR, "img[id=\"captcha_img\"]")
        driver.save_screenshot('captchaImage.png')

        location = captcha_img.location
        size = captcha_img.size

        # Capture the screenshot of the element
        driver.save_screenshot('screenshot.png')

        # Crop the screenshot to the element's dimensions
        left = int(location['x'])
        top = int(location['y'])
        right = int(location['x'] + size['width'])
        bottom = int(location['y'] + size['height'])

        screenshot = Image.open('screenshot.png')
        element_screenshot = screenshot.crop((left, top, right, bottom))
        element_screenshot.save('element_screenshot.png')
        image_path = "element_screenshot.png"
        base64_data = image_to_base64(image_path)
        captcha_text = captcha.solver_captcha(base64_data)
        captcha_input.clear()
        captcha_input.write(captcha_text)
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"btn primary px-5 rounded-pill btn-success btn-rounded-pill btn-depressed xlistener\"]")
        submit_button.click()
    except:
        pass
    sleep(3)

    # Automatically pressing register new visit button
    try:
        register_new_visit_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"btn outline-primary px-4 rounded-pill d-block d-lg-inline-block mb-3 btn-rounded-pill btn-depressed xlistener\"]")
        register_new_visit_button.click()
    except:
        sleep(2)
        try:
            register_new_visit_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"btn outline-primary px-4 rounded-pill d-block d-lg-inline-block mb-3 btn-rounded-pill btn-depressed xlistener\"]")
            register_new_visit_button.click()
        except:
            pass
    sleep(3)

    # Select embassy
    embassy_select = driver.find_element(By.CSS_SELECTOR, "div[class=\"xselect-display form-control\"]")
    embassy_select.click()
    sleep(1)

    # countries = ["India", "UNITED ARAB EMIRATES", "TURKEY"]
    # random_country = random.choice(countries)
    embassy_input = driver.find_element(By.ID, "mega-search-megaEmbassy")
    embassy_input.write(country)
    sleep(1)

    list_item_parent1 = driver.find_element(By.CSS_SELECTOR, "div[class=\"xselect-list-item\"]")
    list_item_parent2 = list_item_parent1.find_element(By.CSS_SELECTOR, "div[class=\"d-flex align-items-center\"]")
    list_item = list_item_parent2.find_element(By.CSS_SELECTOR, "div[class=\"flex-grow-1\"]")
    list_item.click()
    sleep(1)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(3)

    embassy_next_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"btn btn-success btn-rounded-pill btn-depressed xlistener\"]")
    driver.execute_script("arguments[0].click();", embassy_next_button)
    sleep(3)

    # Automatically selecting participant of visit 
    while(True):
        try:
            participant_card = driver.find_elements(By.CSS_SELECTOR, "div[class=\"xradio-card-footer\"]")[1]
            participant_card.click()
            break
        except:
            sleep(2)
            pass
    sleep(3)

    participants_next_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"btn btn-success btn-rounded-pill btn-depressed xlistener\"]")
    driver.execute_script("arguments[0].click();", participants_next_button)
    sleep(5)

    # Automatically selecting visit type
    while(True):
        try:
            element = driver.find_elements(By.CSS_SELECTOR, "div[class=\"xconsult-item-data xlistener-collapse\"]")[7]
            driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
            break
        except:
            sleep(2)
            pass
    sleep(1)
    while(True):
        try:
            radio_button = driver.find_elements(By.CSS_SELECTOR, "input[name=\"EmbassyContactListServiceId\"]")[8]
            radio_button.click()
            break
        except:
            sleep(2)
            pass
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button[class=\"btn btn-success btn-rounded-pill btn-depressed xlistener\"]").click()
    sleep(2)

    # Automatically inputing data
    connection = database.openConnection()
    appointment = database.getRandAppointment(connection)
    database.closeConnection(connection)
    while(True):
        try:
            first_name_input = driver.find_element(By.CSS_SELECTOR, 'input[name=\"User[1][Name]\"]')
            first_name_input.write(appointment["firstname"])
            break
        except:
            sleep(0.5)
            pass

    surname_input = driver.find_element(By.CSS_SELECTOR, "input[name=\"User[1][Surname]\"]")
    surname_input.write(appointment["surname"])

    email_input = driver.find_element(By.CSS_SELECTOR, "input[name=\"User[1][Email]\"]")
    email_input.write("dennis@gmail.com")

    phone_number_input = driver.find_element(By.CSS_SELECTOR, "input[name=\"User[1][Phone]\"]")
    phone_number_input.write("+123456780")

    representation_input = driver.find_element(By.CSS_SELECTOR, "textarea[name=\"User[1][Purpose]\"]")
    representation_input.write(appointment["representation"])
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[class=\"btn btn-success btn-rounded-pill btn-depressed xlistener\"]").click()
    sleep(3)

    # Automatically submit appointment
    while(True):
        try:
            turn_on_reminder_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"btn btn-lg mb-2 alert-reminder-btn d-block d-sm-inline-block btn-rounded-pill btn-depressed xlistener\"]")
            turn_on_reminder_button.click()
            break
        except:
            sleep(0.5)
            pass
    sleep(3)
    agree_checkbox = driver.find_element(By.CSS_SELECTOR, "input[is=\"checkbox-simple\"]")
    agree_checkbox.click()
    sleep(1)

    final_submit_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"btn btn-primary rounded-pill px-4 ml-auto btn-success btn-rounded-pill btn-depressed xlistener\"]")
    final_submit_button.click()
    sleep(3)

    got_it_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"btn btn-success btn-rounded-pill btn-depressed\"]")
    got_it_button.click()
    sleep(3)

    
    return True

run()

