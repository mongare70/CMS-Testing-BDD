from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


@given('I launch browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path='/home/hillary/Desktop/Documents/WebDrivers/chromedriver')
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when('I open application')
def open_application(context):
    context.driver.get('https://content-management-system.netlify.app/')


@when('Enter username "{user}" and password "{pwd}"')
def enter_credentials(context, user, pwd):
    context.driver.find_element_by_id('username').send_keys(user)
    context.driver.find_element_by_id('password').send_keys(pwd)


@when('Click on Login')
def click_on_login(context):
    context.driver.find_element_by_tag_name('button').click()


@then('User must login to the Dashboard page')
def verify_login(context):
    try:
        text = context.driver.find_element_by_xpath('//*[@id="root"]/h1').text
    except:
        context.driver.close()
        assert False, 'Test Failed'

    if text == 'User Dashboard':
        assert True, "Test Passed"


@when('Navigate to "{user}" Profile Page')
def navigate_to_profile(context, user):
    # object of ActionChains
    a = ActionChains(context.driver)
    # identify sub menu element
    m = context.driver.find_element_by_xpath('//*[@id="root"]/nav/ul/li[3]')
    # hover over element
    a.move_to_element(m).perform()
    # identify sub menu element
    n = context.driver.find_element_by_link_text('Profile')
    # hover over element and click
    a.move_to_element(n).click().perform()


@then('Profile Page should display')
def verify_profile(context):
    try:
        text = context.driver.find_element_by_xpath('//*[@id="root"]/div[2]/h1').text
    except:
        context.driver.close()
        assert False, 'Test Failed'

    if text == "Profile":
        context.driver.close()
        assert True, "Test Passed"


@when('Click on Log Out')
def log_out(context):
    # object of ActionChains
    a = ActionChains(context.driver)
    # identify sub menu element
    m = context.driver.find_element_by_xpath('//*[@id="root"]/nav/ul/li[3]')
    # hover over element
    a.move_to_element(m).perform()
    # identify sub menu element
    n = context.driver.find_element_by_xpath('//*[@id="root"]/nav/ul/li[3]/ul/li[2]/button')
    # hover over element and click
    a.move_to_element(n).click().perform()


@then('Login Page should display')
def verify_log_out(context):
    try:
        text = context.driver.find_element_by_xpath('//*[@id="root"]/div[2]/h1[2]').text
    except:
        context.driver.close()
        assert False, 'Test Failed'

    if text == "Log In":
        context.driver.close()
        assert True, "Test Passed"
