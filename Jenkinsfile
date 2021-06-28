pipeline {
    agent { label 'master' }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Code Analysis') {
            steps {
                withSonarQubeEnv('Sonar') {
                // sh 'mvn clean package sonar:sonar'
              }
            }
        }
        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                    // true = set pipeline to UNSTABLE, false = don't
                    waitForQualityGate abortPipeline: true
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
                sh 'sudo cp -r /var/lib/jenkins/workspace/MyGarage /home/ubuntu/WebApps/'
                sh 'sudo systemctl restart mygarage'
            }
        }
    }
}