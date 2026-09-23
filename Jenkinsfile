pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'python --version'
                sh 'python -m compileall src'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest discover -s tests -p "test_*.py"'
            }
        }
    }

    post {
        always {
            echo "CI pipeline completed"
        }
        success {
            echo "Build and tests passed"
        }
        failure {
            echo "Build or tests failed"
        }
    }
}
