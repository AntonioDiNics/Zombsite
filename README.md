# Zombsite

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Description
This is a website made as a task during my HyperionDev software engineering bootcamp. It is simple and has some basic features such as a login, regsiter, voting, and simple information. 
The contents of the website pertains to some weapons from a video game and how to make them. 

## Installation
1. Clone the repository:
  - git clone https://github.com/AntonioDiNics/Zombsite.git

2. Navigate to the project directory:
  - cd Zombsite

3. Build docker:
  - docker build -t zombsite ./

4. Run docker:
  - docker run -p 8000:8000 zombsite
    
4. Open in browser: 
  - type localhost:8000 in browser

## Usage
- **LOGIN**: The user can login with existing credentials.
- **REGISTER**: If the user does not yet have an account, they are able to create an account that will be saved for future login.
- **VIEW STAFF**: Each staff can be clicked on which takes the user to another page which tells the user how to build that staff. 
- **VOTE**: User is able to vote for a staff that they think is best as well as view what other people have voted for. 

## Credits
Developed by [AntonioDiNics](https://github.com/AntonioDiNics).

