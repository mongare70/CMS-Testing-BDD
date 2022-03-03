from behave import *
from selenium import webdriver


@given('I launch Chrome Browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path='/home/hillary/Desktop/Documents/WebDrivers/chromedriver')


@then('I open CMS Homepage')
def open_homepage(context):
    context.driver.get('https://content-management-system.netlify.app/')


@then('Enter username "{user}" and password "{pwd}"')
def enter_credentials(context, user, pwd):
    context.driver.find_element_by_id('username').send_keys(user)
    context.driver.find_element_by_id('password').send_keys(pwd)


@then('Click on login button')
def click_on_login(context):
    context.driver.find_element_by_tag_name('button').click()


@then('User must successfully login to the Dashboard page')
def verify_login(context):
    try:
        context.driver.implicitly_wait(10)
        text = context.driver.find_element_by_xpath('//*[@id="root"]/h1').text
    except:
        context.driver.close()
        assert False, 'Test Failed'

    if text == 'User Dashboard':
        context.driver.close()
        assert True, "Test Passed"
