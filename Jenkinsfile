pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Rozpoczynam budowanie nowego obrazu aplikacji...'
                sh 'docker build -t lab-app:dev ./app'
            }
        }

        stage('Distribute to Workers (Ansible)') {
            steps {
                echo 'Uruchamiam Ansible, aby wysłać obraz na węzły...'
                sh '''
                export ANSIBLE_HOST_KEY_CHECKING=False
                ansible-playbook -i ansible/inventory.ini ansible/playbooks/05-deploy-local-image.yml -u ubuntu --private-key /home/lin/.ssh/id_ed25519
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Aktualizuję manifesty w klastrze...'
                // Jeśli Jenkins zgłosi brak dostępu do klastra,
                // dodamy tutaj ścieżkę do Twojego pliku kubeconfig
                sh 'kubectl apply -f k8s-manifests/'
            }
        }
    }
}
