pipeline {
    agent any
    environment {
        IMAGE_NAME="document-rotation"
    }
    stages {
        stage('Login ECR'){
            // Login to Amazon ECR
            steps{
                withEnv (["AWS_ACCESS_KEY_ID=${env.AWS_ACCESS_KEY_ID}", "AWS_SECRET_ACCESS_KEY=${env.AWS_SECRET_ACCESS_KEY}", "AWS_DEFAULT_REGION=${env.AWS_DEFAULT_REGION}"]){
                    sh "aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin ${REPOSITORY_URI}"
                }
            }
        }

        stage('Build and Push Image') { 
            // Build the Docker image using the specified Dockerfile
            // Should use GIT_COMMIT as tag of image
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
                sh "docker tag ${IMAGE_NAME}:latest ${REPOSITORY_URI}/${IMAGE_NAME}:latest"
                sh "docker push ${REPOSITORY_URI}/${IMAGE_NAME}:latest"
            }
        }
    }
}
