# LangGraph NodeTool SQL Agent

A simple Flask API for querying a database using natural language. The API receives a user query, processes it with a database agent, and returns the result.

## Features

- Exposes a `/askdb` POST endpoint for querying the database.
- Handles errors gracefully and returns appropriate HTTP status codes.
- Modular design with a separate `database_agent` for database logic.

## Requirements

- Python 3.7+
- Flask

Install dependencies:
```bash
pip install flask
```

## Usage

1. **Start the API server:**
    ```bash
    python main.py
    ```

2. **Send a POST request to `/askdb`:**
    - URL: `http://localhost:5000/askdb`
    - Method: `POST`
    - Body (JSON):
      ```json
      {
        "query": "YOUR_DATABASE_QUERY"
      }
      ```

3. **Example using `curl`:**
    ```bash
    curl -X POST http://localhost:5000/askdb -H "Content-Type: application/json" -d "{\"query\": \"SELECT * FROM users;\"}"
    ```

## File Structure

- `main.py` - Flask API entry point.
- `database_agent.py` - Contains the `answer_from_db` function for handling database queries.

## Notes

- Make sure to implement the `answer_from_db` function in `database_agent.py` to connect and query your database.
- Error handling is included for invalid queries and unexpected exceptions.

## License
