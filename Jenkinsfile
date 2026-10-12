pipeline {
    agent any

    stages {
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

        stage('Code Security Scan') {
            steps {
                bat 'python -m bandit -r app'
            }
        }

        stage('Dependency Security Scan') {
            steps {
                bat 'python -m pip_audit'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'D:\\DockerTools\\docker.bat build -t devsecure-pipeline:%BUILD_NUMBER% .'
            }
        }

        stage('Docker Smoke Test') {
            steps {
                bat 'D:\\DockerTools\\docker.bat run --rm devsecure-pipeline:%BUILD_NUMBER% python -c "import app.main; print('Application import successful')"'
            }
        }
    }
}