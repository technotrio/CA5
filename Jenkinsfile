pipeline {
    agent any

    stages {
        stage('Build Database Image') {
            steps {
                script {
                    // Building the Docker image
                    sh 'docker build -t techtrio/ca4 .'

                    // Tag image
                    sh 'docker tag techtrio/ca4 techtrio/ca4:latest'

                    // Push  to Docker Hub
                    sh 'docker push techtrio/ca4:latest'
                }
            }
        }
    }
}
