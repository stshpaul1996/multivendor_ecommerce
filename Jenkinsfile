pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9' // Set the Python version you want to use
    }

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
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv venv
                            venv\\Scripts\\activate
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Run Migrations') {
            steps {
                sh 'python manage.py migrate'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python manage.py test'
            }
        }

        stage('Static Files Collection') {
            steps {
                sh 'python manage.py collectstatic --noinput'
            }
        }

        stage('Docker Build and Deploy') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            docker build -t multivendor_ecommerce .
                            docker-compose up -d
                        '''
                    } else {
                        bat '''
                            docker build -t multivendor_ecommerce .
                            docker-compose up -d
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'deactivate'
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
