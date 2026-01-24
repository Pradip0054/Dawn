# Contributing
## Required Tools
- Docker
- VS Code
- [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Setup Development Environment
- Clone this repo

  ```bash
  git clone git@github.com:BiltuDas1/Dawn.git
  ```

- Open the repo in VS Code
- Use `Ctrl + Shift + P` and then type `Dev Containers: Reopen in Container`
- Wait for sometime, it will download and build the Development Docker Image
- Now Install all the dependencies:
  
  ```bash
  poetry install
  ```

## Run the software
- Create a `.env` file
- Set [Required Environment Variables](./README.md#environment-variables) in the `.env`
- Run the following command to run the software

  ```bash
  poetry run python main.py
  ```
