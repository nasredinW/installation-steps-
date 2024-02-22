# welcome_script.py

import subprocess

def welcome_message():
    return """
    Welcome to UBIAI Tools Solution!
    
    Thank you for joining as a new contributor. We're excited to have you on board.

    To get started, let's set up your development environment using Docker and UBIAI tools.

    Pulling UBIAI Docker images...

    """

def create_empty_docker_compose():
    with open("docker-compose.yaml", "w") as docker_compose_file:
        docker_compose_file.write("# Your Docker Compose configuration goes here.")

def pull_docker_images():
    images_to_pull = [
        "ubiaitools/onpremise-train:latest",
        "ubiaitools/onpremise-be:gpu-v1.7.4",
        "ubiaitools/inference:latest",
        "ubiaitools/onpremise-fe:gpu-v1.12",
        "postgres:latest",
        "redis:alpine"
    ]

    for image in images_to_pull:
        subprocess.run(["docker", "pull", image])

if __name__ == "__main__":
    print(welcome_message())
    print("Pull images started...")
    pull_docker_images()
    create_empty_docker_compose()
    print("Pull images completed. You're ready to go!")
