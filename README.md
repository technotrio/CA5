## Prerequisites
- Docker
- Docker Compose

## Docker Compose Configuration

The `docker-compose.yml` file defines two services:

- `app`: This service represents the web application.
- `db`: This service represents the MySQL database.

Images for both services are pulled from Docker Hub.

## Running the Docker Compose Stack

To run the My App stack, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/technotrio/CA4.git
   cd my-app

2. Start the Docker Compose stack:

   docker-compose up -d

3. Wait for the containers to start. You can check the logs to monitor the progress:

   docker-compose logs -f

4. To stop the stack and remove the containers when you're done, run:

   docker-compose down






