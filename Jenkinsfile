pipeline {
    agent any
    environment {
        IMAGE_NAME="document-rotation"
    }
    stages {
        stage('Login ECR'){
            steps{
                sh '''docker login -u AWS -p $(aws ecr get-login-password --region ${REGION}) ${REPOSITORY_URI}'''
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
