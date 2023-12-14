pipeline {
    agent any
    environment {
        IMAGE_NAME="document-rotation"
    }
    stages {
        stage('Print Environment Variables'){
            steps{
                sh 'printenv'
            }
        }
        stage('Login ECR'){
            steps{
                withEnv (["AWS_ACCESS_KEY_ID=${env.AWS_ACCESS_KEY_ID}", "AWS_SECRET_ACCESS_KEY=${env.AWS_SECRET_ACCESS_KEY}", "AWS_DEFAULT_REGION=${env.AWS_DEFAULT_REGION}"]){
                    sh 'aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 518505801870.dkr.ecr.ap-southeast-1.amazonaws.com'
                }
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
