pipeline {
    agent any

    stages {
        stage('setup') {
            steps {
                sh 'yum install python'
                sh 'python get-pip.py'
                sh 'pip install -r requirements.txt'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
            }
        }
    }
}
