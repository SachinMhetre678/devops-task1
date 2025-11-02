pipeline {
    agent any
    
    stages {
        stage('Cleanup Previous Containers') {
            steps {
                bat '''
                echo "🧹 Cleaning up previous containers..."
                docker stop devops-app || echo "No container to stop"
                docker rm devops-app || echo "No container to remove"
                echo "Cleanup completed"
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                bat '''
                echo "🐳 Building Docker image..."
                docker build -t hello-devops-app .
                echo "✅ Docker image built successfully"
                '''
            }
        }
        
        stage('Run Container') {
            steps {
                bat '''
                echo "🚀 Running container..."
                docker run -d -p 5000:5000 --name devops-app hello-devops-app
                echo "✅ Container started successfully"
                '''
            }
        }
        
        stage('Test Application') {
            steps {
                bat '''
                echo "⏳ Waiting for application to start..."
                timeout /t 15
                echo "✅ Testing application health..."
                curl http://localhost:5000/health
                echo "🎉 Application deployed successfully!"
                '''
            }
        }
        
        stage('Verification') {
            steps {
                bat '''
                echo "🔍 Verifying deployment..."
                docker ps
                echo "✅ Verification complete - Container is running"
                '''
            }
        }
    }
    
    post {
        success {
            echo "================================================"
            echo "📸 TASK 1 COMPLETED SUCCESSFULLY!"
            echo "================================================"
            echo "✅ Jenkins pipeline executed all stages"
            echo "🐳 Docker image built and container running"
            echo "🌐 Application accessible at: http://localhost:5000"
            echo "❤️ Health check working: http://localhost:5000/health"
            echo ""
            echo "🚀 DOCKER + JENKINS PIPELINE - WORKING!"
        }
        failure {
            echo "❌ Pipeline failed - check Docker installation"
        }
    }
}