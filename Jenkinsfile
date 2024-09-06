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
                    // Create virtual environment
                    sh 'python3 -m venv venv'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Activate the virtual environment and install dependencies
                    sh '''
                        # Activate virtual environment and install dependencies
                        . venv/bin/activate
                        pip install --upgrade setuptools
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Migrations') {
            steps {
                script {
                    // Apply migrations using the activated virtual environment
                    sh '''
                        . venv/bin/activate
                        python manage.py migrate
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run tests using the activated virtual environment
                    sh '''
                        . venv/bin/activate
                        python manage.py test
                    '''
                }
            }
        }
        stage('Docker Build and Deploy') {
            steps {
                script {
                    // Build and run Docker container
                    sh '''
                        docker build -t myapp .
                        docker run -d -p 8000:8000 myapp
                    '''
                }
            }
        }
    }
    post {
        always {
            script {
                echo 'Cleaning up workspace...'
                cleanWs()  // Clean workspace
            }
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}




// pipeline {
//     agent any
//     stages {
//         stage('Checkout') {
//             steps {
//                 git branch: 'backend', url: 'https://github.com/stshpaul1996/multivendor_ecommerce.git'
//             }
//         }
//         stage('Setup Python Environment') {
//             steps {
//                 script {
//                     sh 'python3 -m venv venv'  // Create virtual environment
//                     sh 'source venv/bin/activate'  // Activate virtual environment
//                 }
//             }
//         }
//         stage('Install Dependencies') {
//             steps {
//                 script {
//                     sh 'source pip install --upgrade setuptools'  // Upgrade setuptools
//                     sh 'source venv/bin/activate && pip install -r requirements.txt'  // Install dependencies
//                 }
//             }
//         }
//         stage('Run Migrations') {
//             steps {
//                 script {
//                     sh 'source venv/bin/activate && python manage.py migrate'  // Apply migrations
//                 }
//             }
//         }
//         stage('Run Tests') {
//             steps {
//                 script {
//                     sh 'source venv/bin/activate && python manage.py test'  // Run tests
//                 }
//             }
//         }
//         stage('Docker Build and Deploy') {
//             steps {
//                 script {
//                     sh 'docker build -t myapp .'  // Build Docker image
//                     sh 'docker run -d -p 8000:8000 myapp'  // Run Docker container
//                 }
//             }
//         }
//     }
//     post {
//         always {
//             script {
//                 echo 'Cleaning up workspace...'
//                 cleanWs()  // Clean workspace
//             }
//         }
//         success {
//             echo 'Pipeline executed successfully!'
//         }
//         failure {
//             echo 'Pipeline failed!'
//         }
//     }
// }




// pipeline {
//     agent any
//     stages {
//         stage('Checkout') {
//             steps {
//                 git branch: 'backend', url: 'https://github.com/stshpaul1996/multivendor_ecommerce.git'
//             }
//         }
//         stage('Setup Python Environment') {
//             steps {
//                 script {
//                     if (isUnix()) {
//                         sh 'python3 -m venv venv'
//                         sh 'source venv/bin/activate'
//                     } else {
//                         bat 'python -m venv venv'
//                         bat 'venv\\Scripts\\activate'
//                     }
//                 }
//             }
//         }
//         stage('install Dependencies') {
//             steps {
//                 script {
//                     bat 'venv\\Scripts\\pip install --upgrade setuptools'
//                     bat 'venv\\Scripts\\pip install -r requirements.txt' // For Windows
//                 }
//             }
//         }
//         stage('Run Migrations') {
//             steps {
//                 script {
//                     bat 'venv\\Scripts\\python manage.py migrate' // For Windows
//                 }
//             }
//         }
//         stage('Run Tests') {
//             steps {
//                 script {
//                     bat 'venv\\Scripts\\python manage.py test' // Modify if necessary
//                 }
//             }
//         }
//         stage('Docker Build and Deploy') {
//             steps {
//                 script {
//                     bat 'docker build -t myapp .'
//                     bat 'docker run -d -p 8000:8000 myapp'
//                 }
//             }
//         }
//     }
//     post {
//         always {
//             script {
//                 // Windows alternative commands, if cleanup scripts are required
//                 bat 'echo Cleaning up...'
//             }
//         }
//         failure {
//             echo 'Pipeline failed'
//         }
//     }
// }
