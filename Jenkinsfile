pipeline {
    agent any

    stages {
        stage('setup') {
            steps {
                sh 'python3 --version'
                sh 'python3 get-pip.py'
                sh 'pip install -r requirements.txt'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
            }
        }
    }
}
