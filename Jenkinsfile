pipeline {
    agent any

    environment {
        DOCKER_IMAGE_OWNER = 'chkion1234'
        DOCKER_IMAGE_TAG = 'latest'
        DOCKER_TOKEN = credentials('dockerhub')
    }

    stages {
        stage('Clone from SCM') {
            steps {
                sh '''
                rm -rf hello-msa
                git clone https://github.com/chkion1234/hello-msa.git
                '''
            }
        }
        
        stage('Docker Image Building') {
            steps {
                sh '''
                cd hello-msa
                docker build -t ${DOCKER_IMAGE_OWNER}/msa-frontend:${DOCKER_IMAGE_TAG} ./msa-frontend
                docker build -t ${DOCKER_IMAGE_OWNER}/msa-user-service:${DOCKER_IMAGE_TAG} ./msa-user-service
                docker build -t ${DOCKER_IMAGE_OWNER}/msa-product-service:${DOCKER_IMAGE_TAG} ./msa-product-service
                '''
            }
        }
        
        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USR', passwordVariable: 'DOCKER_PWD')]) {
				sh "echo $DOCKER_PWD | docker login -u $DOCKER_USR --password-stdin"
                }
            }
        }
        
        stage('Docker Image Pushing') {
            steps {
                sh '''
                docker push ${DOCKER_IMAGE_OWNER}/msa-frontend:${DOCKER_IMAGE_TAG}
                docker push ${DOCKER_IMAGE_OWNER}/msa-user-service:${DOCKER_IMAGE_TAG}
                docker push ${DOCKER_IMAGE_OWNER}/msa-product-service:${DOCKER_IMAGE_TAG}
                '''
            }
        }
        
        stage('Docker Logout') {
            steps {
                sh '''
                docker logout 
                '''
            }
        }
    }
}
