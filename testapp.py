import unittest 
import app

class testapp(unittest.TestCase):
    def test_getJenkinsUrl(self):
        #Arrange
        expectedUrl = "http://65.0.251.132:8080"

        #Act
        actualUrl = app.getJenkinsUrl()

        #Assert
        self.assertEqual(expectedUrl, actualUrl)