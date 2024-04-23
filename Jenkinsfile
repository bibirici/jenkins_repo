pipeline {
    agent any

    stages {

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
