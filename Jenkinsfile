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
                    // Use Docker Hub credentials
                    withCredentials([usernamePassword(credentialsId: 'Docker_Account', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                    }
                }
            }
        }

        stage('Run Docker Compose') {
            steps {
                script {
                    
                    def flaskImage = sh(script: 'docker pull techtrio/appca4', returnStatus: true) == 0
                    def backendImage = sh(script: 'docker pull techtrio/ca4', returnStatus: true) == 0

                    if (flaskImage && backendImage) {
                        sh 'docker-compose up -d'
                    } else {
                        error 'Required Docker images not found on Docker Hub.'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Docker Compose stack started successfully.'
        }
        failure {
            error 'Failed to start Docker Compose stack.'
        }
    }
<<<<<<< HEAD
}
=======
}
>>>>>>> ace3c1213247854fe085da6df960bb2d8ea5c750
