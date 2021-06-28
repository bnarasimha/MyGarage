pipeline {
    agent { label 'master' }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Unit Tests') { 
            steps {
                sh 'python3 -m unittest tests/unittests/testapp.py'
            }
        }
        stage('Deploy') {
            steps{
                sh 'cp MyGarage /home/ubuntu/WebApps/MyGarage'
                sh 'systemctl restart mygarage'
            }
        }
    }
}