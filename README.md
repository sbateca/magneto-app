# Magneto App

This is the backend of Magneto App. It's built in Python. It allow the users to perform DNA verifications and verify the statistics of verified records.

## Getting Started 🚀

These instructions will allow you to obtain a copy of the project and then run it on your local machine, for development and testing purposes.

### Prerequisites 📋

What things you need to install the software and how to install them.

- **Docker**. You can  donwload it from [Docker official site](https://www.docker.com/get-started/)
- **Chococately** (only for Windows users). [Here](https://docs.chocolatey.org/en-us/choco/setup/) you can find some instructions to install this tool.
- **Make**. You can have here some instructions according your operative system:
    - Windows: Once you have install Chocolatelly, you can install Make using this command:
        ```bash
        choco install make
        ```
    - Linux:
        ```bash
        sudo apt update
        sudo apt install make
        ```
    - MacOs:
        ```bash
        xcode-select --install
        ```


### Running the app 🔧

The following steps will help you tu run the app.


1. Clone the repository:
    ```bash
    git clone https://github.com/sbateca/magneto-app.git
    ```
2. set environment variables:
Before starting the application, you need to set up the following environment variables in your `.env` file. If you do not have a `.env` file, create one in the root directory of the project with this values:
    ```bash
    MAGNETO_DNA_DATA_TABLE="xxxxxx"
    AWS_ACCESS_KEY_ID="xxxxxx"
    AWS_SECRET_ACCESS_KEY="xxxxxx"
    AWS_DEFAULT_REGION="xxxxxx"
    ```
    Get the `.env` values [here](https://some-link.com/): 
3. Build and run the app.
    ```bash
    make up
    ```
This action will start the project and will be available in `http://127.0.0.1:8001` or `localhost:8001`.

## Running the tests ⚙️

To run the tests, use the following command:
  
  ```bash
  make test
  ```

# Test coverage
[![codecov](https://codecov.io/gh/sbateca/magneto-app/branch/main/graph/badge.svg)](https://codecov.io/gh/sbateca/magneto-app)