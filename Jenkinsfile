pipeline {
    agent any

    environment {
        DOCKER_IMAGE_OWNER = 'chkion1234'
        DOCKER_BUILD_TAG = "v20241108.${env.BUILD_NUMBER}"
        DOCKER_TOKEN = credentials('dockerhub')
        GIT_CREDENTIALS = credentials('github_token')
        REPO_URL = 'Yongheech/hello-msa-cd.git'
        COMMIT_MESSAGE = 'Update README.md via Jenkins Pipeline'
    }

    stages {
        stage('clone from SCM') {
            steps {
                sh '''
                rm -rf hello-msa
		git clone https://github.com/Yongheech/hello-msa.git
		'''
            }
        }

        stage('Docker Image Building') {
            steps {
                sh '''
                cd hello-msa
		docker build -t ${DOCKER_IMAGE_OWNER}/msa-frontend:latest -t ${DOCKER_IMAGE_OWNER}/msa-frontend:${DOCKER_BUILD_TAG} ./msa-frontend
		docker build -t ${DOCKER_IMAGE_OWNER}/msa-user-service:latest -t ${DOCKER_IMAGE_OWNER}/msa-user-service:${DOCKER_BUILD_TAG} ./msa-user-service
		docker build -t ${DOCKER_IMAGE_OWNER}/msa-product-service:latest -t ${DOCKER_IMAGE_OWNER}/msa-user-service:${DOCKER_BUILD_TAG} ./msa-product-service
		docker tag ${DOCKER_IMAGE_OWNER}/msa-frontend:latest ${DOCKER_IMAGE_OWNER}/msa-frontend:${DOCKER_BUILD_TAG}
		docker tag ${DOCKER_IMAGE_OWNER}/msa-user-service:latest ${DOCKER_IMAGE_OWNER}/msa-user-service:${DOCKER_BUILD_TAG}
		docker tag ${DOCKER_IMAGE_OWNER}/msa-product-service:latest ${DOCKER_IMAGE_OWNER}/msa-product-service:${DOCKER_BUILD_TAG}
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


        stage('Docker Image pushing') {
            steps {
                sh '''
		docker push ${DOCKER_IMAGE_OWNER}/msa-frontend:latest
		docker push ${DOCKER_IMAGE_OWNER}/msa-user-service:latest
		docker push ${DOCKER_IMAGE_OWNER}/msa-product-service:latest
		docker push ${DOCKER_IMAGE_OWNER}/msa-frontend:${DOCKER_BUILD_TAG}
		docker push ${DOCKER_IMAGE_OWNER}/msa-user-service:${DOCKER_BUILD_TAG}
		docker push ${DOCKER_IMAGE_OWNER}/msa-product-service:${DOCKER_BUILD_TAG}
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
        
        stage('Clone Repository') {
            steps {
                sh '''
                rm -rf hello-msa-cd
                git clone https://github.com/${REPO_URL}
                '''
            }
        }
        
        stage('Modify README.md') {
            steps {
		sh """
		cd hello-msa-cd
		echo "# Updated README" > README.md
		echo "This README was updated by Jenkins Build #${env.BUILD_NUMBER} on \$(date)" >> README.md
		"""
            }
        }

        stage('Commit Changes') {
            steps {
                dir('hello-msa-cd') {
                sh '''
                    git config user.name "Yongheech"
                    git config user.email "alpacatnt@jenkins.com"
                    git add README.md
                    git commit -m "${COMMIT_MESSAGE}"
                '''
                }
            }
        }

        stage('Push Changes') {
            steps {
                dir('hello-msa-cd') {
                sh '''
                    git push https://${GIT_CREDENTIALS_USR}:${GIT_CREDENTIALS_PSW}@github.com/${REPO_URL} main
                '''
                }
            }
        }
        
    }
}
