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
      steps {
      		kubernetesDeploy configs: 'kubernetes.yml', 
		      dockerCredentials: [[credentialsId: 'fra.ocir.io/ptsbm02', url: 'https://fra.ocir.io']], 
		      kubeConfig: [path: ''], kubeconfigId: 'kubeconfig_new', 
		      secretName: 'ptsbm02', 
		      ssh: [sshCredentialsId: '*', sshServer: ''], 
		      textCredentials: [certificateAuthorityData: 'LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURqRENDQW5TZ0F3SUJBZ0lVYXlzemZ0czU2Q3ZFSTNXTEhvVkVJeFo2NjFVd0RRWUpLb1pJaHZjTkFRRUwKQlFBd1hqRUxNQWtHQTFVRUJoTUNWVk14RGpBTUJnTlZCQWdUQlZSbGVHRnpNUTh3RFFZRFZRUUhFd1pCZFhOMAphVzR4RHpBTkJnTlZCQW9UQms5eVlXTnNaVEVNTUFvR0ExVUVDeE1EVDBSWU1ROHdEUVlEVlFRREV3WkxPRk1nClEwRXdIaGNOTVRnd05qRTRNVGd6TXpBd1doY05Nak13TmpFM01UZ3pNekF3V2pCZU1Rc3dDUVlEVlFRR0V3SlYKVXpFT01Bd0dBMVVFQ0JNRlZHVjRZWE14RHpBTkJnTlZCQWNUQmtGMWMzUnBiakVQTUEwR0ExVUVDaE1HVDNKaApZMnhsTVF3d0NnWURWUVFMRXdOUFJGZ3hEekFOQmdOVkJBTVRCa3M0VXlCRFFUQ0NBU0l3RFFZSktvWklodmNOCkFRRUJCUUFEZ2dFUEFEQ0NBUW9DZ2dFQkFPaGFJK0JMTUdidnNsaUxRN3k5UW83Q0ltOE9MVEdpQ3R3K1pmckkKTmhiaW80MStFdjlFdlh6Q2FrcHNubXhHV1VGMU9GZTgrNkZDWW10emlLR1BBckhlTmRwSTRCZDdXY2VJNEFSagoyRzNTSkowak02V3VLZlBmelFHVzFmaW5ZbUJBc3A4cW44RjlCVThXRHFRMnpkZ1h0a1BFUVZ1UnJ6NDAxMExOCnZTbHFLaDE1NEhDKzdCUXpwZzl1Y0tRZlBTV3JQVnBWbFduMVZyMll2L3k1T3ZjalJVRkVOdTg1cTN0YVV4YmUKZzZzc3ZkNjlpekdCalcrbUdUandEVE5sazJ2MWJoZWZlTU5UZEVqWS96aXc0VUxwZWdXKzJTQmc0RyswRkgyKwptVFd4Mld5ZEJESjQrQi93a0V4QUZkd1dsaCtOaWRKSHZEdXM1eHRWVXlyTVI4RUNBd0VBQWFOQ01FQXdEZ1lEClZSMFBBUUgvQkFRREFnRUdNQThHQTFVZEV3RUIvd1FGTUFNQkFmOHdIUVlEVlIwT0JCWUVGQmxvR0ErQS9DTHQKUElKc0NPblhKeVQ4dW95QU1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRRGN6WGlyM0s3MTM3WEV4V3VmYTZoMgpDODNSSGgzWGlUazJpMlVnRDRacnpxZENhNFFwMjc2eUZYM3RoaVNZSHFQSmg4Q2U4Y1hzK2U4YUMzeHFLWEF2CjJSV0FWMVpBQno5aHJYWkYrYmxSTXZTT3M5Y29pRHJzdEZWYlAzeDU1R1h4cnBKa0tCbi85eEhHalZpVDV0cWMKdnRWcXFMUmk1alEyaUZONE5haUVPQmZLU051QkpKOUZYVkRGYSswZjN0dkc5bTJhU0RqRU9lRThWVHRxNFNxUgpuY2RRQkxSL3dDdm9zdG5pek1FL1BjbFlvT2V6ckxVTUQvRTJ6ZkpwazJnRmRrTTNKWnM4UmRYRkRMZzN6dTZ3CmpzdElQaThaSWZ1bm1pT1V3bnRLcGRObUVWV2hYRWo3Wm82eEp1eFhUcG03MUdkZ0tSVjQxdzNKbGY4dHliQkUKLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=', clientCertificateData: 'eyJoZWFkZXIiOnsiQXV0aG9yaXphdGlvbiI6WyJTaWduYXR1cmUgdmVyc2lvbj1cIjFcIixrZXlJZD1cIm9jaWQxLnRlbmFuY3kub2MxLi5hYWFhYWFhYWthb2l3aGc1cWdqbHc1ZGw0bmNlamw3NnU3dmp6a3V0bHo3Zmt3Z2tkaWRrd2N2enVud3Evb2NpZDEudXNlci5vYzEuLmFhYWFhYWFham55ZGtsZGlrbXJlams1eTJ3Y2Nyd2Rvemlxc2R0YWVod2tjbjY3ZTZzZ3N4Z3B2a3FnYS84NzozMTo4Njo1OTo4Mjo4MTo0ZDoyOTpkYjo5MjozZjpiMTo3MjoxYzowMDpiMFwiLGFsZ29yaXRobT1cInJzYS1zaGEyNTZcIixoZWFkZXJzPVwiKHJlcXVlc3QtdGFyZ2V0KSBkYXRlIGhvc3QgeC1jb250ZW50LXNoYTI1NiBjb250ZW50LXR5cGUgY29udGVudC1sZW5ndGhcIixzaWduYXR1cmU9XCJwSFdYSWE2ZHdWZE9QVWxPWGk5aTVmQ0E0Q3JrQ1NvcEx6dkVCSE1XR1hVRDJyeHV0RVA0bnhqL3UxQjZFQzZTQXBLaFJ3ejVzZ1lENWVLanI1SW9ISEo4c043MWV6RE9GZFZuUG13VXZkeloxaVNUaFA2Z3BXdTVrRzVSbGh5NWROcjV6NUQwdVVUUFVxZXZaUGhvd2pTRy9vYyt1KzNudmk3b010a0ZseW9wcFlmbVdpSUhRMDlYb1R3Z3RsdHV6UWRTUTIxZ3lWNXpKUHFsZ2lySkljVHh0TzJmd3VwNTZla1ZNUFN4SFBSZkNBTnBYR3FNQ1NHcVMvSktvQkhCdXJyS1FHeEJKYUdEQTZ6aEh6N05Gbi9hNFJjU3FINGkyQUhwRHAwMnFyV0hpblUya3o0QnA4UzBlREdPSXFsMUl1M3U5MGpaTmxYWmp1NlB4WmRPS2c9PVwiIl0sIkNvbnRlbnQtTGVuZ3RoIjpbIjAiXSwiQ29udGVudC1UeXBlIjpbImFwcGxpY2F0aW9uL2pzb24iXSwiRGF0ZSI6WyJUdWUsIDE5IEp1biAyMDE4IDExOjE3OjM1IEdNVCJdLCJYLUNvbnRlbnQtU2hhMjU2IjpbIjQ3REVRcGo4SEJTYSsvVEltVys1SkNldVFlUmttNU5NcEpXWkczaFN1RlU9Il19LCJib2R5Ijp7InRva2VuVmVyc2lvbiI6IjEuMC4wIiwiZXhwaXJhdGlvbiI6MjU5MjAwMDAwMDAwMDAwMH0sImhvc3QiOiJjb250YWluZXJlbmdpbmUuZXUtZnJhbmtmdXJ0LTEub3JhY2xlY2xvdWQuY29tIiwicmVxdWVzdF91cmkiOiIvYXBpLzIwMTgwMjIyL2NsdXN0ZXJzL29jaWQxLmNsdXN0ZXIub2MxLmV1LWZyYW5rZnVydC0xLmFhYWFhYWFhYWZxdGluenptaTJ0bXlydW12cXdnb2p5bXpyZGNuenJndTRkc3lqd2djNHRpbmRkZ250ZC9rdWJlY29uZmlnL2NvbnRlbnQifQ==', clientKeyData: '', serverUrl: 'https://c4tinddgntd.eu-frankfurt-1.clusters.oci.oraclecloud.com:6443']
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
