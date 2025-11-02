pipeline {
    agent any
    
    stages {
        stage('Build and Run Docker') {
            steps {
                bat '''
                echo "🚀 Starting Task 1 - Docker + Jenkins"
                echo "Current directory:"
                dir
                
                echo "🐳 Building Docker image..."
                docker build -t hello-devops-app .
                
                echo "🚀 Running container..."
                docker run -d -p 5000:5000 --name devops-app hello-devops-app
                
                echo "⏳ Waiting for app to start..."
                ping -n 10 127.0.0.1 > nul
                
                echo "✅ Testing application..."
                curl http://localhost:5000/health
                
                echo "🎉 TASK 1 COMPLETED SUCCESSFULLY!"
                '''
            }
        }
    }
    
    post {
        success {
            echo "📸 TAKE THESE SCREENSHOTS FOR SUBMISSION:"
            echo "1. This Jenkins pipeline success"
            echo "2. Running container: 'docker ps'"
            echo "3. Browser: http://localhost:5000"
            echo "4. Health check: 'curl http://localhost:5000/health'"
        }
    }
}