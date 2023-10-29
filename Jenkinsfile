pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker Login') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: '6beba5b8-9507-4b39-86c5-da901d3a0209', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"}
    
                    }
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
                            sh 'docker tag techtrio/ca4 techtrio/ca4:latest'
                           
                        }
                    }
                }

        stage('Push to Docker Hub') {
            steps {
                script {
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

