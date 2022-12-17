pipeline {
	agent {
		label 'python-pipeline'
		}
	stages {
		stage ("pull scm python") {
			steps {
				git branch: 'python', url: 'https://github.com/wssrronak/python-pipeline.git'
				}
			}
		stage ("Build") {
			steps {
				sh 'python3 -V'
				sh 'python3 cp.py'
				}
			}
		stage ("Test") {
			steps {
				sh 'python3 test.py'
				}
			}
		}
	}
