pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing crud-flask-webapp application ...'
            }
        }

        stage('Release') {
            when { branch 'main' }
            steps {
                echo 'Releasing crud-flask-webapp application ...'
            }
        }

        stage('Deploy') {
            when { branch 'main' }
            steps {
                echo 'Deploing crud-flask-webapp application ...'
            }
        }
    }

    post {
        always {
            echo 'Some stuff to always do after stages ..'
        }
    }
}