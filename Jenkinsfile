pipeline {
    agent any
    environment {
        REGION = "ap-southeast-1"
        REPOSITORY_URI = "518505801870.dkr.ecr.ap-southeast-1.amazonaws.com/document-rotation"
    }

    stages {
        stage('Login ECR'){
            steps{
                sh """aws ecr get-login-password --region ${REGION} | sudo docker login --username AWS --password-stdin ${REPOSITORY_URI}"""
            }
        }
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
