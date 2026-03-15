from fastapi import FastAPI, HTTPException
from datetime import datetime
import pytz

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


@app.get("/convert")
def convert_time(
    datetime_str: str,
    from_tz: str,
    to_tz: str,
):
    """
    Convert a datetime string from one timezone to another.

    - **datetime_str**: datetime in ISO 8601 format, e.g. `2026-03-15T20:00:00`
    - **from_tz**: source timezone, e.g. `Europe/Moscow`
    - **to_tz**: target timezone, e.g. `America/New_York`
    """
    try:
        source_tz = pytz.timezone(from_tz)
    except pytz.UnknownTimeZoneError:
        raise HTTPException(status_code=400, detail=f"Unknown timezone: {from_tz}")
    try:
        target_tz = pytz.timezone(to_tz)
    except pytz.UnknownTimeZoneError:
        raise HTTPException(status_code=400, detail=f"Unknown timezone: {to_tz}")

    try:
        dt = datetime.fromisoformat(datetime_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid datetime format, use ISO 8601: YYYY-MM-DDTHH:MM:SS")

    dt_localized = source_tz.localize(dt)
    converted = dt_localized.astimezone(target_tz)

    return {
        "original": dt_localized.isoformat(),
        "converted": converted.isoformat(),
        "from_tz": from_tz,
        "to_tz": to_tz,
    }
