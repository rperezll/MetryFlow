
# MetryFlow Backend

> [!IMPORTANT]  
> The development of MetryFlow Backend is not yet finished.

**MetryFlow Backend** is a centralized system for processing and managing telemetry data, specifically focused on the collection, storage, and analysis of event metrics. This backend is designed to receive telemetry events from various applications, store them in a MongoDB database, and provide endpoints to retrieve and query these events. With FastAPI as the main framework, it is optimized for performance and scalability.

## Tech Stack

- **Framework**: FastAPI (Python 3.12)
- **Database**: MongoDB (NoSQL)
- **Web Server**: Uvicorn (ASGI server)
- **ORM**: Motor (Asynchronous MongoDB driver)

## Installation

To set up the project locally install the dependencies using `pip` and the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install all the necessary dependencies and libraries required for the application.

## Development Setup

For **development purposes**, you can use the following command to run the server with FastAPI's development tools, enabling hot-reloading:

```bash
fastapi dev main.py
```

This will start the FastAPI server with auto-reload, so any code changes will automatically be applied.

## Production Setup

In production, use the following command:

```bash
fastapi run main.py
```

This will start the application without hot-reloading, optimized for production.

## Endpoints

### `/health`

Checks the health of the application and verifies if MongoDB is available.

- **Method**: GET
- **Response**: JSON with `status` and `database` keys.

### `/telemetry/events`

Receives telemetry events from applications and stores them in the MongoDB database.

- **Method**: POST
- **Body**: JSON object containing telemetry event data.
- **Response**: Confirmation message with the inserted event ID.

### `/metrics`

Retrieves a list of stored telemetry events, filtered by query parameters like `installation_id`, `framework`, and `platform`.

- **Method**: GET
- **Query Parameters**:
  - `installation_id` (optional)
  - `framework` (optional)
  - `platform` (optional)
  - `limit` (default: 10)
  - `skip` (default: 0)

## License 📝

- [GPL-3.0 license]()