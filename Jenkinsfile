pipeline {
    agent { label 'awsec2' }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
    }
}