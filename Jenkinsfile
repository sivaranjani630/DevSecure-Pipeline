pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Update Pip') {
            steps {
                bat 'python -m pip install --upgrade pip'
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