pipeline {
    agent {
        docker { image 'alpine' }
    }

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
            steps {
                echo 'Releasing crud-flask-webapp application ...'
            }
        }

        stage('Deploy') {
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