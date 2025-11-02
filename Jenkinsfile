pipeline {
    agent any
    
    environment {
        DOCKER_HOST = "tcp://localhost:2375"
    }
    
    stages {
        stage('Test Docker Connection') {
            steps {
                bat '''
                echo "Testing Docker TCP connection..."
                docker -H tcp://localhost:2375 ps
                echo "Docker TCP test complete"
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                bat '''
                echo "Building image via TCP..."
                docker -H tcp://localhost:2375 build -t hello-devops-app .
                echo "Build completed via TCP"
                '''
            }
        }
        
        stage('Run Container') {
            steps {
                bat '''
                echo "Running container via TCP..."
                docker -H tcp://localhost:2375 run -d -p 5000:5000 --name jenkins-app hello-devops-app
                echo "Container started via TCP"
                '''
            }
        }
        
        stage('Test Application') {
            steps {
                bat '''
                echo "Waiting for app to start..."
                timeout /t 10
                echo "Testing application..."
                curl http://localhost:5000/health
                echo "Application test complete!"
                '''
            }
        }
    }
    
    post {
        success {
            echo "🎉 JENKINS + DOCKER PIPELINE SUCCESS!"
            echo "📸 Take screenshots of this successful pipeline"
        }
    }
}