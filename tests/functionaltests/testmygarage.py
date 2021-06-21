# import unittest
# from selenium import webdriver
# from chromedriver_py import binary_path 

# class testMyGarage(unittest.TestCase):
#     def setup(self):
#         self.driver = webdriver.Chrome(executable_path=binary_path)
    
#     def test_MyTools(self):
#         self.driver.get("http://localhost:5000")
#         elem = self.driver.find_element_by_id("mytools")
#         self.assertIsNotNone(elem)

#         #assert "Python" in driver.title

#     if __name__ == '__main__':
#         unittest.main()



# import all required frameworks
import unittest
from selenium import webdriver
from chromedriver_py import binary_path 
from selenium.webdriver.common.keys import Keys

# inherit TestCase Class and create a new test class
class PythonOrgSearch(unittest.TestCase):

	# initialization of webdriver
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=binary_path)

	# Test case method. It should always start with test_
	def test_search_in_python_org(self):
		
		# get driver
		driver = self.driver
		# get python.org using selenium
		driver.get("http://localhost:5000")

		# assertion to confirm if title has python keyword in it
		#self.assertIn("Python", driver.title)

		# locate element using name
		elem = driver.find_element_by_id("mytools")
        
		# send data
		#elem.send_keys("pycon")

		# recieve data
		#elem.send_keys(Keys.RETURN)
		#assert "No results found." not in driver.page_source

	# cleanup method called after every test performed
	def tearDown(self):
		self.driver.close()

# execute the script
if __name__ == "__main__":
	unittest.main()
