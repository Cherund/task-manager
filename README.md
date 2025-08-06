### Hexlet tests and linter status:
[![Actions Status](https://github.com/Cherund/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Cherund/python-project-52/actions)
[![Actions Status](https://github.com/Cherund/python-project-52/actions/workflows/self-check.yml/badge.svg)](https://github.com/Cherund/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/bdfddf7136e5bbfe475f/maintainability)](https://codeclimate.com/github/Cherund/python-project-52/maintainability)

# Task Manager

## Overview

Task Manager is a web application built with Django that allows users to create, manage, and track tasks. It supports user authentication, task categorization, and task status updates.

## Features
- User registration and authentication
- Create, update, and delete tasks
- Task status updates (to-do, in progress, completed)
- Assign categories to tasks
- Filter tasks by status or category

## Technologies Used
- Python 3.x
- Django 3.x
- PostgreSQL
- HTML/Bootstrap for frontend
- Docker for containerization

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Poetry (dependency management)
- PostgreSQL
- Docker (optional)

## Local Setup
**After cloning the repository and setting up PostgreSQL DB**
   
1. **Install dependencies:**
```
make install
```

2. **Set up environment variables:** Create a `.env` file and define:
```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://task_manager_user:your-password@localhost/task_manager
```

3. **Run database migrations:**
```
make migrate
```

4. **Run the development server:**
```
make run
```

**Access the application:** Navigate to `http://127.0.0.1:8000/` in your browser.

### Running Tests

**Run the project's tests:**
```
make test
```


### [Project on render](https://task-manager-b4n1.onrender.com)
