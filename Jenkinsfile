pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = credentials('TechTrio')
        DOCKER_HUB_PASSWORD = credentials('techtrio_1998')
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
