pipeline {
	agent {
		label 'python-pipeline'
		}
	stages {
		stage ("pull scm") {
			steps {
				git ''
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
