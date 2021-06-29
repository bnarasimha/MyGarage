pipeline {
    agent { label 'master' }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Code Analysis') {
            environment {
                scannerHome = tool 'SonarQubeScanner'
            }
            steps {
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -D sonar.projectKey=bnarasimha_MyGarage -D sonar.organization=bnarasimha"
              }
            }
        }
        stage('Unit Tests') { 
            steps {
                sh 'python3 -m unittest tests/unittests/testapp.py'
            }
        }
        stage('Deploy') {
            steps{
                sh 'pip install wheel'
                sh 'python3 setup.py bdist_wheel'
                // sh 'sudo cp -r /var/lib/jenkins/workspace/MyGarage /home/ubuntu/WebApps/'
                // sh 'sudo systemctl restart mygarage'
            }
        }
    }
}