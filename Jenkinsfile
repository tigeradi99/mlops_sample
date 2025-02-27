import groovy.transform.Field

@Field def INITIALIZE_STATUS = 'NOT RUN'
@Field def PREPROCESS_DATA = 'NOT RUN'
@Field def TRAIN_MODEL = 'NOT RUN'
@Field def TEST_STATUS = 'NOT RUN'
@Field def MODEL_SERVE = 'NOT RUN'
@Field def MODEL_SERVE_TEST = 'NOT RUN'
@Field def S3_DEPLOY_STATUS = 'NOT RUN'

pipeline {
    agent any
    
    stages {

        //stage('Clone Repository') {
        //    steps {
        //        // Clone Repository
        //        script {
        //            echo 'Cloning GitHub Repository...'
        //            checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'mlops-git-token', url: 'https://github.com/iQuantC/MLOps01.git']])
        //        }
        //    }
        //}

        stage('Intialize'){
            steps{
                script{
                    bat 'pip install -r requirements.txt"'
                }
            }
            post{
                success{
                    script{INITIALIZE_STATUS = 'SUCCESS'}
                }
                failure{
                    script{INITIALIZE_STATUS = 'FAILED'}
                }
            }
        }

        stage('Load and Preprocess Data') {
            steps {
                // Lint code
                script {
                    echo 'Loading and Preprocessing Data...'
                    bat "python load_data.py"
                }
            }
            post{
                success{
                    script{PREPROCESS_DATA = 'SUCCESS'}
                }
                failure{
                    script{PREPROCESS_DATA = 'FAILED'}
                }
            }
        }

        stage('Train Model') {
            steps {
                // Lint code
                script {
                    echo 'Training model...'
                    bat "python model_training.py"
                }
            }
            post{
                success{
                    script{TRAIN_MODEL = 'SUCCESS'}
                }
                failure{
                    script{TRAIN_MODEL = 'FAILED'}
                }
            }
        }

        stage('Model Evaluation') {
            steps {
                // Pytest code
                script {
                    echo 'Evaluating Model...'
                    bat "pytest model_evaluation.py"
                }
            }
            post{
                success{
                    script{TEST_STATUS = 'SUCCESS'}
                }
                failure{
                    script{TEST_STATUS = 'FAILED'}
                }
            }
        }

        stage('Start Serving Model') {
            steps {
                // Pytest code
                script {
                    echo 'Serving Model for testing...'
                    bat "python app.py"
                }
            }
            post{
                success{
                    script{MODEL_SERVE = 'SUCCESS'}
                }
                failure{
                    script{MODEL_SERVE = 'FAILED'}
                }
            }
        }

        stage('Test Model Server') {
            steps {
                // Pytest code
                script {
                    echo 'Testing served model...'
                    // Test the server with sample values
                    bat '''
                        curl -X POST "http://127.0.0.1:5000/predict" ^
                        -H "Content-Type: application/json" ^
                        -d "{\\"features\\": [13.2, 2.77, 2.51, 18.5, 103.0, 1.15, 2.61, 0.26, 1.46, 3.0, 1.05, 3.33, 820.0]}"
                    '''
                }
            }
            post{
                success{
                    script{MODEL_SERVE_TEST = 'SUCCESS'}
                }
                failure{
                    script{MODEL_SERVE_TEST = 'FAILED'}
                }
            }
        }      
    }

    post{
        always {
            cleanWS()
        }
    }
}