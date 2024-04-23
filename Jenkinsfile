pipeline {
    agent any

    stages {
        stage('setup') {
            steps {
                sh 'cd /Users/abibiric/.jenkins/workspace/pipeline1_git'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Trigger build1') {
            steps {
                echo 'Triggering build1'
                build(job: 'test_build1_github')
            }
        }

        stage('Trigger build2') {
            steps {
                echo 'Triggering build2'
                build(job: 'test_build2_github')
            }
        }
    }
}
