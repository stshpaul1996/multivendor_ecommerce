pipeline {
    agent any

    environment {
        // Define environment variables here, if needed
        PYTHON_ENV = 'venv' // virtual environment name
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from the Git repository
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    // Set up virtual environment and install dependencies
                    sh '''
                    python3 -m venv ${PYTHON_ENV}
                    source ${PYTHON_ENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Migrations') {
            steps {
                script {
                    // Run database migrations
                    sh '''
                    source ${PYTHON_ENV}/bin/activate
                    python manage.py migrate
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run unit tests
                    sh '''
                    source ${PYTHON_ENV}/bin/activate
                    python manage.py test
                    '''
                }
            }
        }

        stage('Static Files Collection') {
            steps {
                script {
                    // Collect static files
                    sh '''
                    source ${PYTHON_ENV}/bin/activate
                    python manage.py collectstatic --noinput
                    '''
                }
            }
        }

        stage('Docker Build and Deploy') {
            steps {
                script {
                    // Build and deploy using Docker
                    sh '''
                    docker build -t multivendor_ecommerce:latest .
                    docker-compose down
                    docker-compose up -d
                    '''
                }
            }
        }
    }

    post {
        always {
            // Clean up virtual environment
            script {
                sh '''
                deactivate || true
                rm -rf ${PYTHON_ENV}
                '''
            }
        }

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
