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
        sh 'sudo docker login -u \'ptsbm02/radu.dobrinescu@oracle.com\' -p \'_QgxIb5H)zmmBAzEX#ll\' fra.ocir.io'
        sh 'sudo docker push fra.ocir.io/ptsbm02/devopsdemoapp:1'
      }
    }
    stage('Deploy to Stage'){
	 withKubeConfig(caCertificate: 'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURqRENDQW5TZ0F3SUJBZ0lVYXlzemZ0czU2Q3ZFSTNXTEhvVkVJeFo2NjFVd0RRWUpLb1pJaHZjTkFRRUwKQlFBd1hqRUxNQWtHQTFVRUJoTUNWVk14RGpBTUJnTlZCQWdUQlZSbGVHRnpNUTh3RFFZRFZRUUhFd1pCZFhOMAphVzR4RHpBTkJnTlZCQW9UQms5eVlXTnNaVEVNTUFvR0ExVUVDeE1EVDBSWU1ROHdEUVlEVlFRREV3WkxPRk1nClEwRXdIaGNOTVRnd05qRTRNVGd6TXpBd1doY05Nak13TmpFM01UZ3pNekF3V2pCZU1Rc3dDUVlEVlFRR0V3SlYKVXpFT01Bd0dBMVVFQ0JNRlZHVjRZWE14RHpBTkJnTlZCQWNUQmtGMWMzUnBiakVQTUEwR0ExVUVDaE1HVDNKaApZMnhsTVF3d0NnWURWUVFMRXdOUFJGZ3hEekFOQmdOVkJBTVRCa3M0VXlCRFFUQ0NBU0l3RFFZSktvWklodmNOCkFRRUJCUUFEZ2dFUEFEQ0NBUW9DZ2dFQkFPaGFJK0JMTUdidnNsaUxRN3k5UW83Q0ltOE9MVEdpQ3R3K1pmckkKTmhiaW80MStFdjlFdlh6Q2FrcHNubXhHV1VGMU9GZTgrNkZDWW10emlLR1BBckhlTmRwSTRCZDdXY2VJNEFSagoyRzNTSkowak02V3VLZlBmelFHVzFmaW5ZbUJBc3A4cW44RjlCVThXRHFRMnpkZ1h0a1BFUVZ1UnJ6NDAxMExOCnZTbHFLaDE1NEhDKzdCUXpwZzl1Y0tRZlBTV3JQVnBWbFduMVZyMll2L3k1T3ZjalJVRkVOdTg1cTN0YVV4YmUKZzZzc3ZkNjlpekdCalcrbUdUandEVE5sazJ2MWJoZWZlTU5UZEVqWS96aXc0VUxwZWdXKzJTQmc0RyswRkgyKwptVFd4Mld5ZEJESjQrQi93a0V4QUZkd1dsaCtOaWRKSHZEdXM1eHRWVXlyTVI4RUNBd0VBQWFOQ01FQXdEZ1lEClZSMFBBUUgvQkFRREFnRUdNQThHQTFVZEV3RUIvd1FGTUFNQkFmOHdIUVlEVlIwT0JCWUVGQmxvR0ErQS9DTHQKUElKc0NPblhKeVQ4dW95QU1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRRGN6WGlyM0s3MTM3WEV4V3VmYTZoMgpDODNSSGgzWGlUazJpMlVnRDRacnpxZENhNFFwMjc2eUZYM3RoaVNZSHFQSmg4Q2U4Y1hzK2U4YUMzeHFLWEF2CjJSV0FWMVpBQno5aHJYWkYrYmxSTXZTT3M5Y29pRHJzdEZWYlAzeDU1R1h4cnBKa0tCbi85eEhHalZpVDV0cWMKdnRWcXFMUmk1alEyaUZONE5haUVPQmZLU051QkpKOUZYVkRGYSswZjN0dkc5bTJhU0RqRU9lRThWVHRxNFNxUgpuY2RRQkxSL3dDdm9zdG5pek1FL1BjbFlvT2V6ckxVTUQvRTJ6ZkpwazJnRmRrTTNKWnM4UmRYRkRMZzN6dTZ3CmpzdElQaThaSWZ1bm1pT1V3bnRLcGRObUVWV2hYRWo3Wm82eEp1eFhUcG03MUdkZ0tSVjQxdzNKbGY4dHliQkUKLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=', credentialsId: 'kube', serverUrl: 'https://c4tinddgntd.eu-frankfurt-1.clusters.oci.oraclecloud.com:6443') {
		steps {
			sh 'kubectl --namespace=stage apply -f kubernetes.yml'
		}
	 }
	// some block
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
