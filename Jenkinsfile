pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the local Dockerfile in the same directory
                    sh 'docker build -t techtrio/appca4 .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // No need to log in if you're not pushing to Docker Hub
                    sh 'docker push techtrio/appca4'
                }
            }
        }
    }

    post {
        success {
            echo "Docker image built successfully."
        }
        failure {
            error "Failed to build the Docker image."
        }
    }
}
