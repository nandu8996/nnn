pipeline {
    agent any
        stages {
            stage ('Checkout code') {
                steps {
                    git credentialsId: 'NANDITHA', url : "https://github.com/nandu8996/nnn.git", branch: "main"
                }
            }

            stage ("Install dependencies") {
                steps {
                    bat '''
                        python -m venv venv
                        call venv\\Scrpits\\activate
                        pip install --upgrade pip
                        pip install pytest
                    '''
                }
            }

            stage ('Test') {
                steps {
                    bat '''
                        call venv\\Scripts\\activate
                        pytest test.py
                    '''
                }
            }

            stage ('Deploy') {
                steps {
                    bat '''
                        echo "Deplying feature"
                        call venv\\Scripts\\activate
                        python login.py
                    '''
                }
            }
        }
}