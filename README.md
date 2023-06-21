# Streaming FlanT5-XL Model Results From Docker Container

This project demonstrates how to stream live results of the FlanT5-XL model from a Docker container using Flask, Flask-SocketIO, and Transformers. The client sends a prompt to the server, the model generates a result, and the server streams each token back to the client in real-time.

## Prerequisites

- Python 3.10
- Docker
- Poetry for Python dependency management
- Basic knowledge of Flask, Docker, SocketIO, and Transformer models

## Project Structure

- **Server Code:** Contains the server implementation which loads the FlanT5-XL model and listens to client connections.
- **Client Code:** Contains the client code which sends the prompt to the server and receives the response.
- **Docker Scripts:** Contains the scripts to build and run the Docker image.
- **pyproject.toml:** Configuration for building the Docker image.

## Getting Started

1. Clone the repository: 

    ```bash
    git clone https://github.com/rp-86/streaming_flanT5.git
    ```

2. Navigate to the project directory:

    ```bash
    cd streaming_flanT5
    ```

3. Install the project dependencies with Poetry:

    ```bash
    poetry install
    ```

4. Export the project dependencies to a requirements.txt file:

    ```bash
    poetry run poe requirements
    ```

5. Build the Docker image:

    ```bash
    poetry run poe build-image 
    ```

6. Run the Docker image:

    ```bash
    poetry run poe run-image
    ```

7. Open a new terminal and run the client:

    ```bash
    python client.py --prompt "Your prompt here"
    ```

## Notes

- Please note that in the `docker-build.sh` script, you need to replace `"$DOCKERFILE"` and `"$BASE_DIR"` with the location of your Dockerfile and the base directory of your project, respectively. 
- Also, replace `"$IMAGE"` in `docker-run.sh` with the name of your Docker image.
- Replace the base image in Dockerfile with the suitable image

## References

1. Flask official documentation: [https://flask.palletsprojects.com/en/2.0.x/](https://flask.palletsprojects.com/en/2.0.x/)
2. Socket.IO documentation: [https://socket.io/docs/v4](https://socket.io/docs/v4)
3. Transformers library by Hugging Face: [https://huggingface.co/transformers/](https://huggingface.co/transformers/)
4. Docker official documentation: [https://docs.docker.com/get-started/overview/](https://docs.docker.com/get-started/overview/)
5. T5 Model paper: [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683)
