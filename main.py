from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Time API")


@app.get("/time")
def get_server_time():
    """Returns the current server time."""
    return {"server_time": datetime.now().isoformat()}


@app.get("/date")
def get_server_date():
    """Returns the current server date."""
    return {"server_date": datetime.now().date().isoformat()}


@app.get("/datetime")
def get_server_datetime():
    """Returns the current server date and time separately."""
    now = datetime.now()
    return {
        "date": now.date().isoformat(),
        "time": now.time().isoformat(),
        "datetime": now.isoformat(),
    }
