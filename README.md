# Flask Microblog Application

## Project Overview
This Flask application is a simple microblogging platform where users can create accounts, log in, and post messages. It utilizes Flask, SQLAlchemy, Flask-Migrate, and Flask-Login to handle user authentication and database interactions efficiently.

## Features
- **User Authentication:** Login, logout, and registration functionalities.
- **Posting:** Users can write and view posts once logged in.
- **Database Integration:** Using SQLAlchemy for ORM and Flask-Migrate for migration tasks.

## Installation

### Prerequisites
- Python 3.6+
- Flask
- A virtual environment (recommended)

### Setup and Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/microblog.git
cd microblog

# Optional: Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install required packages
pip install -r requirements.txt
