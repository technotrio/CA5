pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'TechTrio'
        DOCKER_HUB_PASSWORD = 'techtrio_1998'
    }

    stages {
        stage('Docker Login') {
            steps {
                script {
                    sh "docker login -u $DOCKER_HUB_USERNAME -p $DOCKER_HUB_PASSWORD"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Building the Docker image 
                    sh 'docker build -t techtrio/ca4 .'
                }
            }
        }

        stage('Tag Image') {
            steps {
                script {
                    // Tag the Docker image
                    sh 'docker tag techtrio/ca4 techtrio/ca4:latest'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    sh 'docker push techtrio/ca4:latest'
                }
            }
        }
    }

    post {
        success {
            echo "SUCCESS."
        }
        failure {
            error "FAILED."
        }
    }
}
