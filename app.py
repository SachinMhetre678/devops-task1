from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_devops():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello DevOps</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: white;
                text-align: center;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
            }
            h1 {
                font-size: 3em;
                margin-bottom: 20px;
            }
            .build-info {
                background: rgba(0, 0, 0, 0.3);
                padding: 10px;
                border-radius: 5px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Hello DevOps!</h1>
            <p>GitHub + Jenkins + Docker Pipeline</p>
            <p>This app is running in a Docker container!</p>
            <div class="build-info">
                <p>✅ CI/CD Pipeline Successful</p>
                <p>🐳 Containerized with Docker</p>
                <p>⚙️ Automated with Jenkins</p>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy', 'service': 'hello-devops-app', 'version': '1.0'}

@app.route('/jenkins')
def jenkins_info():
    return {'pipeline': 'success', 'tools': ['Docker', 'Jenkins', 'GitHub']}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)