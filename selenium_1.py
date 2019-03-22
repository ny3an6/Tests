from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
 
opts = Options()
opts.set_headless()
assert opts.headless  # без графического интерфейса.
 
browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')

search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()

results = browser.find_elements_by_class_name('result')
print(results)