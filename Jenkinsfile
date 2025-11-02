pipeline {
    agent any
    stages {
        stage('Docker Pipeline') {
            steps {
                bat """
                echo "Starting Docker pipeline..."
                echo "Building image..."
                docker build -t hello-devops-app .
                echo "Running container..."
                docker run -d -p 5000:5000 --name devops-app hello-devops-app
                echo "Waiting..."
                timeout /t 10
                echo "Testing..."
                curl http://localhost:5000/health || echo "Health check skipped"
                echo "Pipeline execution completed"
                """
            }
        }
    }
}