pipeline {
    agent { label 'master' }

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Deploy') {
            steps{
                echo 'copy to webapps folder'
            }
        }
    }
}