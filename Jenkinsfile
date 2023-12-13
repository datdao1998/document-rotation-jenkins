pipeline {
    agent any

    stages {
        stage('Login ECR'){
            steps{
                echo 'Repo name : ${REPO_NAME}'
                // sh 'aws ecr get-login-password --region ${REGION} | sudo docker login --username AWS --password-stdin ${REPO_NAME}'
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
