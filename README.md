# Basic Fullstack Project

A simple fullstack demonstration application with a FastAPI server, a Socket Server backend, and a frontend.

In this project, the FastAPI server and the socket server are two independent backend components that don't directly interact with each other. They serve different purposes and demonstrate different ways to implement server functionality:

FastAPI Server: Uses a modern Python web framework with built-in features like:
OpenAPI documentation
Request/response validation
Dependency injection
Async support

Socket Server: Uses low-level Python socket programming to:
Handle HTTP requests manually
Parse HTTP headers and body
Format HTTP responses





## Project Structure

```
.
├── backend/
│   ├── fastapi_server/
│   │   ├── main.py      # FastAPI application setup
│   │   └── APIs.py      # API endpoint definitions
│   └── socket_server/
│       └── server.py    # Basic HTTP socket server
└── frontend/            # Frontend application

```

## Backend

### FastAPI Server

The FastAPI server provides a RESTful API with the following endpoints:

- `GET /` - Health check endpoint
- `GET /api/messages` - Get all messages
- `GET /api/messages/{message_id}` - Get a specific message
- `POST /api/messages` - Create a new message

To run the FastAPI server:

```bash
cd backend/fastapi_server
python -m uvicorn main:app --reload --port 8001
```

Once running, you can access the Swagger UI documentation at `http://localhost:8001/docs`.

### Socket Server

A basic HTTP server implemented using Python's socket library, supporting the following endpoints:

- `GET /` - Home page
- `GET /api/message` - Returns a message as JSON

To run the Socket Server:

```bash
cd backend/socket_server
python server.py
```

The server will run on `http://localhost:8002`.

## Frontend

The frontend application demonstrates communication with both backend servers.

To run the frontend (if it uses npm):

```bash
cd frontend
npm install
npm run dev
```

## Development

### Prerequisites

- Python 3.8+
- Node.js and npm (for frontend)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Shawn-Dong/basic_fullstack.git
   cd basic_fullstack
   ```

2. Set up Python environment
   ```bash
   # Optional: Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install backend dependencies
   pip install fastapi uvicorn
   ```

3. Set up frontend dependencies
   ```bash
   cd frontend
   npm install
   ```

## License

This project is for demonstration purposes.