
import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return process.returncode, output.decode('utf-8'), error.decode('utf-8')

# Update the package index
run_command('sudo apt-get update')

# Install necessary dependencies
run_command('sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common')

# Add Docker's official GPG key
run_command('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg')

# Add the Docker stable repository
docker_repo_command = 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null'
run_command(docker_repo_command)

# Install Docker
run_command('sudo apt-get update')
run_command('sudo apt-get install -y docker-ce docker-ce-cli containerd.io')

# Add your user to the docker group (to run Docker without sudo)
run_command(f'sudo usermod -aG docker {subprocess.check_output("whoami", shell=True).decode().strip()}')

# Restart your system or log out and back in to apply group changes

# Download the Docker Compose binary
docker_compose_command = 'sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
run_command(docker_compose_command)

# Apply executable permissions to the binary
run_command('sudo chmod +x /usr/local/bin/docker-compose')

# Verify the installation
return_code, output, error = run_command('docker-compose --version')
print(output.strip() if return_code == 0 else error.strip())

