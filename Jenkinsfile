pipeline {
    stages {
        stage("Hello") {
            agent {
                docker {
                    image 'python:3.5.0'
                    alwaysPull false
                }
            }
            steps {
                sh "echo Hello world"
            }
        }
    }
}
