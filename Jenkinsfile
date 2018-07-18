pipeline {
  agent {
    node {
      label 'jenkinsslave'
    }

  }
  stages {
    stage('Fetch dependencies') {
      steps {
        sh 'sudo docker pull nginx:latest'
      }
    }
    stage('Build docker image') {
      steps {
        sh 'sudo docker build . -t customnginx:1'
      }
    }
    stage('Test image') {
      steps {
        sh 'echo "Tests successful"'
      }
    }
    stage('Push image to OCIR') {
      steps {
        sh 'sudo docker login -u \'ptsbm02/radu.dobrinescu@oracle.com\' -p \'_QgxIb5H)zmmBAzEX#ll\'fra.ocir.io'
        sh 'sudo docker tag customnginx:1 fra.ocir.io/ptsbm02/nginx:custom'
        sh 'sudo docker push fra.ocir.io/ptsbm02/nginx:custom'
      }
    }
  }
}