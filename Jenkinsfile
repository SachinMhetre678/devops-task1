pipeline {
    agent any
    
    environment {
        APP_NAME = "hello-devops-app"
        CONTAINER_NAME = "hello-devops-container-${BUILD_ID}"
    }
    
    stages {
        stage('Checkout GitHub') {
            steps {
                checkout scm
                echo "✅ Code checked out from GitHub"
                sh 'ls -la'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    echo "🐳 Building Docker image from GitHub code..."
                    sh "docker build -t ${APP_NAME}:${BUILD_ID} ."
                    sh "docker tag ${APP_NAME}:${BUILD_ID} ${APP_NAME}:latest"
                    sh "docker images | grep ${APP_NAME}"
                }
            }
        }
        
        stage('Run Container') {
            steps {
                script {
                    echo "🚀 Running container..."
                    // Cleanup any existing container
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                    
                    // Run new container
                    sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${APP_NAME}:${BUILD_ID}"
                    sh "docker ps | grep ${CONTAINER_NAME}"
                }
            }
        }
        
        stage('Test Application') {
            steps {
                script {
                    echo "✅ Testing application..."
                    sleep 10
                    sh "curl -f http://localhost:5000/"
                    sh "curl -f http://localhost:5000/health"
                    sh "curl -f http://localhost:5000/jenkins"
                    echo "🎉 All tests passed!"
                }
            }
        }
    }
    
    post {
        always {
            echo "🏁 Pipeline execution completed - Build ${BUILD_ID}"
            sh "docker images | grep ${APP_NAME}"
        }
        success {
            echo "📸 SCREENSHOT TIME - TASK 1 COMPLETE!"
            echo "1. Jenkins pipeline success"
            echo "2. GitHub repository"
            echo "3. Running container: docker ps"
            echo "4. Browser: http://localhost:5000"
            echo "5. Health endpoint: http://localhost:5000/health"
            echo "6. Jenkins info: http://localhost:5000/jenkins"
            
            // Keep container running for screenshots
            echo "🔗 Application URLs:"
            echo "   Main: http://localhost:5000"
            echo "   Health: http://localhost:5000/health"
            echo "   Jenkins: http://localhost:5000/jenkins"
        }
        failure {
            echo "❌ Pipeline failed!"
            // Cleanup on failure
            sh "docker stop ${CONTAINER_NAME} || true"
            sh "docker rm ${CONTAINER_NAME} || true"
        }
    }
}