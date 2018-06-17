pipeline {
  agent {
    docker {
      image 'ubuntu:latest'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'cat /etc/os-release'
        sh 'ls'
      }
    }
  }
}
