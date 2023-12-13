pipeline {
    agent any
    environment {
        IMAGE_NAME="document-rotation"
    }
    stages {
        stage('Login ECR'){
            steps{
                sh "/usr/local/bin/aws ecr get-login-password --region ${REGION} | sudo docker login --username AWS --password-stdin ${REPOSITORY_URI}"
            }
        }
        stage('Build Dockerfile') { 
            // Build the Docker image using the specified Dockerfile
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
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
