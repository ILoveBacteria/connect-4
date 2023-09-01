# Connect-4

[![License: MIT](https://img.shields.io/github/license/ILoveBacteria/connect-4)](https://github.com/ILoveBacteria/connect-4/blob/master/LICENSE)
[![Issues](https://img.shields.io/github/issues/ILoveBacteria/connect-4)](https://github.com/ILoveBacteria/connect-4/issues)
[![Forks](https://img.shields.io/github/forks/ILoveBacteria/connect-4)](https://github.com/ILoveBacteria/connect-4/network/members)
![Stars](https://img.shields.io/github/stars/ILoveBacteria/connect-4)
![Watchers](https://img.shields.io/github/watchers/ILoveBacteria/connect-4)
[![Last commit](https://img.shields.io/github/last-commit/ILoveBacteria/connect-4)](https://github.com/ILoveBacteria/connect-4/commits/master)
![python version](https://img.shields.io/github/pipenv/locked/python-version/ILoveBacteria/connect-4?logo=python&logoColor=white)
![npm version](https://img.shields.io/badge/npm-8.19-blue?logo=npm&logoColor=white)
![Workflow](https://img.shields.io/github/actions/workflow/status/ILoveBacteria/connect-4/test.yml?logo=github&label=test)
![Workflow](https://img.shields.io/github/actions/workflow/status/ILoveBacteria/connect-4/node_build.yml?logo=github&label=build+web-app)
[![wiki](https://img.shields.io/badge/wiki-read_the_documention-white?logo=github)](https://github.com/ILoveBacteria/connect-4/wiki)
![GitHub tag](https://img.shields.io/github/v/tag/ILoveBacteria/connect-4?color=lightblue&label=last+tag)
![GitHub release](https://img.shields.io/github/v/release/ILoveBacteria/connect-4?color=green)
![GitHub repo size](https://img.shields.io/github/repo-size/ILoveBacteria/connect-4)
[![Docker](https://img.shields.io/badge/Docker-086dd7?logo=docker&logoColor=white)](https://hub.docker.com/r/ilovebacteria/connect-4)

[![connect-4-gif](https://github.com/ILoveBacteria/connect-4/blob/master/assets/connect-4.gif)](https://github.com/ILoveBacteria/connect-4/blob/master/assets/connect-4.gif)

## Table of Contents

- [Description](#description)
- [How To Run The Project](#how-to-run-the-project)
- [Train the AI](#train-the-ai)
- [What technologies and libraries I used](#what-technologies-and-libraries-i-used)

## Description

This is my AI course final project. I implemented a connect-4 game with a GUI and a simple AI. 
The AI uses the **minimax algorithm** with alpha-beta pruning to find the best move and **reinforcement learning**.

Read the [wiki](https://github.com/ILoveBacteria/connect-4/wiki) for more information about the project and 
How implemented the heuristic function and the Q-Learning.

## How To Run The Project

### Docker

#### How to run the Docker image

```shell
$ docker run -p 5000:5000  ilovebacteria/connect-4:latest
```

#### Enviroment Variables

- `HOST_ADDR`: The host address. (default `127.0.0.1`)
- `DEBUG`: The flask debug mode. (default `False`)

### Manual

1. You have to install [Python](https://www.python.org/downloads/) and [pipenv](https://pypi.org/project/pipenv/) and 
[npm](https://www.npmjs.com/get-npm).
2. Clone the repository.
3. Open the terminal in the project folder and run these commands to install dependencies.
   ```shell script
   pipenv install
   npm install
   ```
   
4. Run this `npm` command to build the project.
   ```shell script
   npm run build
   ```
   
5. Run this `pipenv` command to run the Flask server.
   ```shell script
   pipenv run server
   ```
   
6. Open the browser and go to `http://localhost:5000/`.

## Train the AI

In the Q-Learning, 2 agents play against each other. At the end of each game, the winning agent will be rewarded with 
`1000` and the loser agent will be punished with `-1000`. Both agents will be rewarded `0` if the game ends with a draw.

`connect_4` package provides a CLI. You can use it to train the AI. It will create `q_table.csv` file if it doesn't exist. 
If it exists, it will load the Q-Table from it and continue training.

The Q-Table has 4 columns. The first 3 columns are the state of the board and action, and the last column is the Q-Value.

```shell script
pipenv run python -m connect_4 train --count-games 10
```

## What technologies and libraries I used

- [Flask](https://flask.palletsprojects.com/en/)
- [Pandas](https://pandas.pydata.org/)
- multipledispatch
- [typer](https://typer.tiangolo.com/)
- [React](https://reactjs.org/)
- [Webpack](https://webpack.js.org/)
- [Babel](https://babeljs.io/)
- [Bootstrap](https://getbootstrap.com/)
