pipeline {
    agent any

    stages {
        stage('Build Dockerfile') { 
            // Build the Docker image using the specified Dockerfile
            script {
                dockerImage = docker.build('document-rotation', '-f Dockerfile .')
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
