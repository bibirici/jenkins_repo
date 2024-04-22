pipeline {
    agent any

    stages {
        stage('setup') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
            }
        }
    }
}
