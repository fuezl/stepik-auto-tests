from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    AUTHORIZATION_MAIL = (By.CSS_SELECTOR, '[name="login-username"]')
    AUTHORIZATION_PASSWORD = (By.CSS_SELECTOR, '[name="login-password"]')
    AUTHORIZATION_FORGOT_PASSWORD = (By.CSS_SELECTOR, '.well>p>a')
    AUTHORIZATION_SUBMIT = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTRATION_MAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTRATION_CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')
