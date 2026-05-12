pipeline {
    agent any

    stages {
        stage('checkout scm') {
            steps {
                git branch: 'main', url: 'https://github.com/VatsalSolanki-01/randomverse-api.git'
            }
        }
        stage('build'){
            steps{
                sh '''
                    docker build -t vatsalsolanki19/randomverse-api:latest .
                '''
            }
        }
        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                sh 'docker push vatsalsolanki19/randomverse-api:latest'
            }
        }
        stage('Deploy To Railway') {
            steps {
                sh 'railway up'
            }
        }
    }
}
