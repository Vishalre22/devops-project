pipeline  {
    agent any

    stages  {
        stage('Build Docker Image') {
            steps  {
                sh 'docker build -t vishalaramur/devops-app:latest .'
            }
        }
        stage('Push Image to Docker Hub')  {
            steps  {
                withCredentials([usernamePassword(credentialsId: 'dockerhub' , usernameVariable: 'DOCKER_USER' , passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                    docker login -u $DOCKER_USER -p $DOCKER_PASS
                    docker push vishalaramur/devops-app:latest
                    '''

                }
            }
        }
        stage('Deploy to kubernetes')  {
            steps  {
                 sh 'kubectl apply -f k8s/'
            }
        }
    }
}
