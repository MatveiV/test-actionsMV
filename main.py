from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Time API")


@app.get("/time")
def get_server_time():
    """Returns the current server time."""
    return {"server_time": datetime.now().isoformat()}
