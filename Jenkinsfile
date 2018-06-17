pipeline {
  agent {
    docker {
      image 'ubuntu:lastest'
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
