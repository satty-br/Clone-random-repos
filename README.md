# Clone-Random-Repos
## A Python Script for Creating Fake Repositories
This project provides a single Python script (main.py) designed to a fictional organization with random repositories for Proof-of-Concept (PoC) testing of security analysis tools (SAST, SCA) or CI/CD pipelines.

## Features
Generates Random Repositories: Creates a specified number of repositories with various names and another github repos content.
Customizable Content: Allows customization of the content types (Python, JavaScript, etc.) .
Clones Repositories: Clones the generated repositories locally and clone to new repos.
Flexible Use Case: Serves as a PoC for security analysis tools, CI/CD pipelines, and exploring functionalities of these tools.

## Installation
Clone this repository:
´´´´
git clone https://github.com/satty-br/Clone-random-repos.git
´´´´´

### Install required libraries:

´´´´
cd clone-random-repos
pip install -r requirements.txt
´´´´´

## Usage

Run the script with desired arguments:

´´´´
python main.py --org orgname --num_repos 10 --content_type python
´´´´

Use o código com cuidado.
content_copy
--org: name of org to clone 
--num_repos: Number of repositories to create (default: 100 max:1000).
--content_type: Type of code to generate (java, python, etc.) (default: java).
--token: Github token, if not set ill try use GITHUB_TOKEN enviroment from your system
Example Usage
This command will create 10 fake Python repositories with medium complexity and clone them into the fake_repos directory:

Be cautious when using this script in production environments or sharing the generated repositories publicly.

## Contributing
We welcome contributions to improve this project. Feel free to submit pull requests with enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
