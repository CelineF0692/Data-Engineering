College Data ETL Project

## Overview

This ETL (Extract, Transform, Load) pipeline processes college data using Python for scripting, MySQL for data storage, and Docker for hosting the MySQL database. It demonstrates automated data extraction from various sources, data transformation and cleaning, and loading into a MySQL database for further analysis.

## Features

- **Data Extraction**: Automated Python scripts fetch data from public APIs and datasets.
- **Data Transformation**: Scripts clean, validate, and transform data into a structured format.
- **Data Loading**: Processed data is loaded into a MySQL database for analysis.
- **Docker Integration**: Docker is used to manage the MySQL database environment, ensuring consistency across different setups.
- **Data Analysis**: Includes basic data analysis examples using SQL queries and Python.

## Prerequisites

Before you start, make sure you have installed:
- Docker
- Python 3.8 or later
- Required Python packages (`requirements.txt` will be provided)

## Setup

### 1. Environment Configuration

Create a `.env` file in the project root with necessary MySQL configurations:

```
MYSQL_ROOT_PASSWORD=celine
MYSQL_DATABASE=ETL_Project
MYSQL_USER=root
MYSQL_PASSWORD=celine
```

### 2. Launch MySQL Container

Build and start the MySQL container using Docker Compose:

```
docker-compose up -d
```

This command will initialize a MySQL database in a Docker container as per the settings defined in `docker-compose.yml`.

### 3. Install Python Dependencies

Install the necessary Python packages using:

```
pip install -r requirements.txt
```

### 4. Running the ETL Pipeline

Execute the ETL scripts directly on your host machine:

```
python path/to/your/ETL project.py
```

Ensure the script is configured to connect to the MySQL database running inside the Docker container.

## Accessing the Database

To interact with the MySQL database, use the following command:

```
docker exec -it ETL_Project mysql -u root -p ETL_Project
```
## Contributing

We welcome contributions! Feel free to fork the repository, make changes, and submit pull requests. If you have any suggestions or encounter issues, please open an issue in the GitHub repository.

## License

This project is licensed under the MIT License. See the LICENSE file in the repository for more details.

---
