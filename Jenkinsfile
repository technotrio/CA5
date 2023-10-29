pipeline {
    agent any

    stages {
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Docker Hub credentials ID in Jenkins
                    def dockerHubCredentials = credentials('6beba5b8-9507-4b39-86c5-da901d3a0209')

                    
                    withCredentials([usernamePassword(credentialsId: dockerHubCredentials, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        // Authenticate with Docker Hub
                        sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    }

                    // Building the Docker image
                    sh 'docker build -t techtrio/ca4 .'

                    // Tagging image
                    sh 'docker tag techtrio/ca4 techtrio/ca4:latest'

                    // Push to Docker Hub
                    sh 'docker push techtrio/ca4:latest'
                }
            }
        }
    }
}
