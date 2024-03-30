pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building crud-flask-webapp application ...'
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
                echo 'Deploying crud-flask-webapp application ...'
            }
        }
    }

    post {
        always {
            echo 'Some stuff to always do after stages ..'
        }
    }
}