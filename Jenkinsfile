pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = credentials('6beba5b8-9507-4b39-86c5-da901d3a0209')
        DOCKER_HUB_PASSWORD = credentials('6beba5b8-9507-4b39-86c5-da901d3a0209')
    }

    stages {
        stage('Build Database Image') {
            steps {
                script {
                    // Logging in to Docker Hub
                    sh "docker login -u ${DOCKER_HUB_USERNAME} -p ${DOCKER_HUB_PASSWORD}"

                    // Building the Docker image
                    sh 'docker build -t techtrio/ca4 .'

                    // Tag image
                    sh 'docker tag techtrio/ca4 techtrio/ca4:latest'

                    // Push to Docker Hub
                    sh 'docker push techtrio/ca4:latest'

                    // Log out from Docker Hub
                    sh 'docker logout'
                }
            }
        }
    }
}
