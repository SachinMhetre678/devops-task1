pipeline {
    agent any
    
    environment {
        APP_NAME = "hello-devops-app"
        CONTAINER_NAME = "devops-container-${BUILD_ID}"
    }
    
    stages {
        stage('Cleanup') {
            steps {
                script {
                    echo "🧹 Cleaning up previous containers..."
                    bat 'docker stop devops-container || echo "No container to stop"'
                    bat 'docker rm devops-container || echo "No container to remove"'
                    bat 'docker ps -a'
                }
            }
        }
        
        stage('Checkout GitHub') {
            steps {
                checkout scm
                echo "✅ Code checked out from GitHub"
                bat 'dir'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    echo "🐳 Building Docker image..."
                    bat "docker build -t ${APP_NAME}:${BUILD_ID} ."
                    bat "docker images | findstr ${APP_NAME}"
                }
            }
        }
        
        stage('Run Container') {
            steps {
                script {
                    echo "🚀 Running container..."
                    bat "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${APP_NAME}:${BUILD_ID}"
                    timeout(time: 10, unit: 'SECONDS') {
                        bat "docker ps | findstr ${CONTAINER_NAME}"
                    }
                }
            }
        }
        
        stage('Test Application') {
            steps {
                script {
                    echo "✅ Testing application..."
                    sleep 10
                    bat 'curl -f http://localhost:5000/health'
                    echo "🎉 Application deployed successfully!"
                }
            }
        }
    }
    
    post {
        always {
            echo "🏁 Pipeline execution completed - Build ${BUILD_ID}"
        }
        success {
            echo "================================================"
            echo "📸 TASK 1 COMPLETE - TAKE SCREENSHOTS NOW!"
            echo "================================================"
            echo "1. ✅ This Jenkins pipeline success"
            echo "2. 🐳 Running container: 'docker ps'"
            echo "3. 🌐 Browser: http://localhost:5000"
            echo "4. ❤️ Health check: 'curl http://localhost:5000/health'"
            echo ""
            echo "🚀 Task 1: Docker + Jenkins - COMPLETED!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}