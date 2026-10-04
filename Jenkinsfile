pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Security Scan') {
            steps {
                bat 'python -m bandit -r app'
            }
        }

        stage('Dependency Security Scan') {
            steps {
                bat 'python -m pip_audit'
            }
        }
    }
}