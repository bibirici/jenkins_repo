pipeline {
    agent any

    stages {
        stage('setup') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
            }
        }
    }
}
