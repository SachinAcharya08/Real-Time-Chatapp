# ChatApp

A real-time chat application built with Django REST Framework, Django Channels, WebSockets, and React.

## Tech Stack

### Backend

* Django
* Django REST Framework
* Django Channels
* Redis
* WebSockets
* JWT Authentication
* MySQL

### Frontend

* React
* Vite

## Features

* User authentication with JWT
* Chat threads
* User-based thread access
* REST APIs for chat functionality
* Real-time messaging using WebSockets
* Redis channel layer
* Django Channels consumers
* WebSocket JWT authentication

## Project Structure

```text
chatapp/
├── apps/
│   └── chats/
│       ├── channels_middleware.py
│       ├── consumers.py
│       ├── routing.py
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       └── urls.py
│
├── config/
│   ├── asgi.py
│   ├── settings.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
├── .env
└── .gitignore
```

## Prerequisites

Before running the project, install:

* Python 3.14+
* MySQL
* Redis
* Node.js and npm

## Backend Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd chatapp
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

#### macOS / Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=3306
```

> Never commit your `.env` file or expose your secret key.

### 5. Set up MySQL

Make sure MySQL is installed and running.

Create the database specified by `DB_NAME`.

Then run:

```bash
python manage.py migrate
```

### 6. Start Redis

Make sure Redis is installed and running.

On macOS with Homebrew:

```bash
brew services start redis
```

Check that Redis is running:

```bash
redis-cli ping
```

You should get:

```text
PONG
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Start the backend

```bash
python manage.py runserver
```

The backend will run at:

```text
http://127.0.0.1:8000/
```

## WebSocket Architecture

The application uses Django Channels and Redis for real-time communication.

```text
React Client
     │
     │ WebSocket
     ▼
Django ASGI
     │
     ▼
WebSocket Routing
     │
     ▼
Consumer
     │
     ├── Connect
     ├── Authenticate
     ├── Join Group
     ├── Receive Message
     ├── Save Message
     ├── Group Send
     └── Disconnect
           │
           ▼
         Redis
      Channel Layer
```

## WebSocket Flow

When a user connects to a chat:

1. The client establishes a WebSocket connection.
2. The WebSocket request is authenticated using JWT.
3. The consumer identifies the chat thread.
4. The connection joins the corresponding channel group.
5. Messages are saved to the database.
6. Messages are sent to connected users through the channel group.
7. When a user disconnects, their channel is removed from the group.

## Environment Variables

| Variable      | Description         |
| ------------- | ------------------- |
| `SECRET_KEY`  | Django secret key   |
| `DEBUG`       | Django debug mode   |
| `DB_NAME`     | MySQL database name |
| `DB_USER`     | MySQL username      |
| `DB_PASSWORD` | MySQL password      |
| `DB_HOST`     | MySQL host          |
| `DB_PORT`     | MySQL port          |

## Development

Run the Django development server with:

```bash
python manage.py runserver
```

Make sure MySQL and Redis are running before using the application.

## Status

This project is currently under development.

It is being built to learn and implement:

* Django REST Framework
* Django Channels
* WebSockets
* JWT authentication
* Redis channel layers
* Real-time communication
* React-Django integration

## Future Improvements

* Online/offline user status
* Typing indicators
* Message read status
* Notifications
* Improved error handling
* Message delivery status
* Production deployment
