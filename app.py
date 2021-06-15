from flask import Flask, render_template
from constants import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', Urls=getUrls())

def getUrls():
    urls = {"jenkinsUrl" : getJenkinsUrl(), 
            "blogUrl" : getBlogUrl(), 
            "flipItApiUrl" : getFlipItApiUrl(),
            "scrumGuideUrl" : getScrumGuideUrl(),
            "flipItUrl" : getFlipItUrl(),
            "codeSnippetsUrl" : getCodeSnippetsUrl(),
            "resumeUrl" : getResumeUrl()
    }
    return urls

def getJenkinsUrl():
    return JENKINS_URL

def getBlogUrl():
    return BLOG_URL

def getFlipItApiUrl():
    return FLIPITAPI_URL

def getScrumGuideUrl():
    return SCRUM_GUIDE_URL

def getFlipItUrl():
    return FLIPIT_URL 

def getCodeSnippetsUrl():
    return CODESNIPPETS_URL

def getResumeUrl():
    return RESUME_URL

if __name__ == "__main__":
    app.run(host="localhost", port=5000)