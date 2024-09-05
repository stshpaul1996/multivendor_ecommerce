pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'backend', url: 'https://github.com/stshpaul1996/multivendor_ecommerce.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m venv venv'
                        sh 'source venv/bin/activate'
                    } else {
                        bat 'python -m venv venv'
                        bat 'venv\\Scripts\\activate'
                    }
                }
            }
        }
        stage('install Dependencies') {
            steps {
                script {
                    bat 'venv\\Scripts\\pip install -r requirements.txt' // For Windows
                }
            }
        }
        stage('Run Migrations') {
            steps {
                script {
                    bat 'venv\\Scripts\\python manage.py migrate' // For Windows
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    bat 'venv\\Scripts\\python manage.py test' // Modify if necessary
                }
            }
        }
        stage('Docker Build and Deploy') {
            steps {
                script {
                    bat 'docker build -t myapp .'
                    bat 'docker run -d -p 8000:8000 myapp'
                }
            }
        }
    }
    post {
        always {
            script {
                // Windows alternative commands, if cleanup scripts are required
                bat 'echo Cleaning up...'
            }
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
