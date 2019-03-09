import time
from selenium import webdriver
 
driver = webdriver.Firefox() # создали экзмепляр класса
driver.get("http://192.168.5.119/") # указали что работаем с с данным URL
# assert "Python" in driver.title - ???


def data(l, p, log_name, pass_name):
#def data():
	try:
		login = driver.find_element_by_name(l).send_keys(log_name) # помещаем в переменную поле с именем q
		#login.send_keys(log_name) # заполняем поле 
		password = driver.find_element_by_name(p).send_keys(pass_name)
		#password.send_keys(pass_name) 
		button = driver.find_element_by_class_name("ant-btn-primary")
		button.submit() # elem.send_keys(Keys.return)
	except:
		print()
		print("Invalid login or password")
	time.sleep(2)
	try:
		driver.find_element_by_class_name("ant-layout-content")
		print()
		print('Succes')
	except:
		print()
		print("No such fields")
	#except:
	
    close = input("Enter a key to close app")
    if close = 'exit':
        driver.close()	
	else:
		pass
		
 #assert "No results found." not in driver.page_source
l = input("Enter name of first field: ")
log_name = input("Enter name of:" )
p = input("Enter name of second field: ")
pass_name = input("Enter name of: ")
data(l, p, log_name, pass_name)
#data()
print(driver.name)

# driver.close()

