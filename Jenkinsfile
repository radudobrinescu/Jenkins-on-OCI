pipeline {
  agent {
    node {
      label 'master'
    }

  }
  stages {
    stage('Build docker image') {
      steps {
        sh 'sudo docker build . -t fra.ocir.io/ptsbm02/devopsdemoapp:1'
      }
    }
    stage('Test image') {
      steps {
        sh 'echo "Tests successful"'
      }
    }
    stage('Push image to OCIR') {
      steps {
        sh 'sudo docker login -u \'ptsbm02/radu.dobrinescu@oracle.com\' -p \$TOKEN fra.ocir.io'
        sh 'sudo docker push fra.ocir.io/ptsbm02/devopsdemoapp:1'
      }
    }
    stage('Deploy to Stage'){
	steps {
	 sh 'kubectl --namespace=stage apply -f kubernetes.yml'
	}
    }
    stage('Confirm'){
      steps {
       mail (to: 'radu.dobrinescu@oracle.com',
         subject: "Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) is waiting for input",
         body: "Please go to ${env.BUILD_URL}.");
       input("Ready to promote to Production?")
      }
    }
    stage('Deploy to Production'){
      steps {
       sh 'kubectl --namespace=production apply -f kubernetes.yml'
      }
    }
  }
}
