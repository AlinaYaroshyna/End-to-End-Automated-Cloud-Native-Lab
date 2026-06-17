pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Rozpoczynam budowanie nowego obrazu aplikacji...'
                sh 'docker build -t lab-app:dev ./app'
            }
        }
        
        // UPEWNIJ SIĘ, ŻE TEN ETAP POJAWIA SIĘ TYLKO RAZ
        stage('Distribute to Workers (Ansible)') {
            steps {
                echo 'Zapisuję obraz na dysku Jenkinsa...'
                sh 'docker save -o /tmp/lab-app.tar lab-app:dev'

                echo 'Uruchamiam Ansible, aby wysłać obraz na węzły...'
                sh '''
                export ANSIBLE_HOST_KEY_CHECKING=False
                ansible-playbook -i ansible/inventory.ini ansible/playbooks/05-deploy-local-image.yml -u ubuntu --private-key /home/lin/.ssh/id_ed25519 -vvv
                '''
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                echo 'Aktualizuję manifesty w klastrze...'
                sh 'kubectl apply -f k8s-manifests/'
            }
        }
    }
}
