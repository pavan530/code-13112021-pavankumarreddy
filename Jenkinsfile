#!/usr/bin/env groovy
pipeline {
  agent any

  options {
    disableConcurrentBuilds()
  }

  environment {
    // ENV variables goes here
  }

  stages {
    stage('Building Docker Image: sophia target flybuys airflow image') {
      environment {
        CFN_ENVIRONMENT = 'datasvcsdev'
        ENVIRONMENT = 'dev'
      }
      steps {
        script {
          node {
            checkout scm
            def dockerBuild = docker.build("image_name:latest", "--no-cache" -f ./Dockerfile .")
              withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
              credentialsId: "credentailsId"]]) {
              docker.withRegistry("some ECR endpoint") {
                dockerBuild.push()
              }
            }
          }
        }
      }
    }
  }
}

    