import unittest 
import app
import constants

class testapp(unittest.TestCase):
    def test_getJenkinsUrl(self):
        #Arrange
        expectedUrl = constants.JENKINS_URL

        #Act
        actualUrl = app.getJenkinsUrl()

        #Assert
        self.assertEqual(expectedUrl, actualUrl)

    def test_getBlogUrl(self):
        #Arrange
        expectedUrl = constants.BLOG_URL

        #Act
        actualUrl = app.getBlogUrl()

        #Assert
        self.assertEqual(expectedUrl, actualUrl)

    def test_getFlipItApiUrl(self):
        #Arrange
        expectedUrl = constants.FLIPITAPI_URL

        #Act
        actualUrl = app.getFlipItApiUrl()

        #Assert
        self.assertEqual(expectedUrl, actualUrl)

    def test_getScrumGuideUrl(self):
        #Arrange
        expectedUrl = constants.SCRUM_GUIDE_URL

        #Act
        actualUrl = app.getScrumGuideUrl()

        #Assert
        self.assertEqual(expectedUrl, actualUrl)

    def test_getFlipItUrl(self):
        #Arrange
        expectedUrl = constants.FLIPIT_URL

        #Act
        actualUrl = app.getFlipItUrl()

        #Assert
        self.assertEqual(expectedUrl, actualUrl)