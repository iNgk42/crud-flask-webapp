pipeline {
    agent any

    environment {
        APP_IMAGE_NAME = 'ingk42/siflaweb'
        APP_IMAGE_TAG = 'v0.0.$BUILD_ID'
        REGISTRY_CREDENTIALS = credentials('docker-registry')
    }

    stages {
        stage('Build application docker image') {
            steps {
                sh 'docker build -t $APP_IMAGE_NAME .'
            }
        }

        stage('Test application in container') {
            agent {
                docker { image 'nginx' }
            }

            steps {
                sh 'apk update' 
                sh 'apk add curl'
                //sh 'curl localhost:5000'
                sh 'curl localhost'
            }
        }

        stage('Release') {
            when { branch 'main' }

            steps {
                sh 'docker tag $APP_IMAGE_NAME $APP_IMAGE_NAME:latest'
                sh 'docker tag $APP_IMAGE_NAME $APP_IMAGE_NAME:$APP_IMAGE_TAG'
                sh('echo $REGISTRY_CREDENTIALS_PSW | docker login -u $REGISTRY_CREDENTIALS_USR --password-stdin')
                sh 'docker push $APP_IMAGE_NAME:$APP_IMAGE_TAG'
                sh 'docker push $APP_IMAGE_NAME:latest'
                sh 'docker logout'
            }
        }

        stage('Deploy') {
            when { branch 'main' }

            steps {
                echo 'Deploying siflaweb application ...'
            }
        }
    }

    post {
        always {
            sh 'docker images -q | xargs docker rmi -f'
        }
    }
}