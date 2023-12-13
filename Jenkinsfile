pipeline {
    agent any

    stages {
        stage('Build Dockerfile') { 
            // Build the Docker image using the specified Dockerfile
            steps {
                sh 'docker build -t document-rotation .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing something..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying something..'
            }
        }
    }
}
