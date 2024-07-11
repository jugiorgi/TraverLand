import pytest
import uuid
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="Database interaction to create a trip")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trip_info = {
        "id": trip_id,
        "destination": "Salt Lake City",
        "start_date": datetime.now().isoformat(),
        "end_date": (datetime.now() + timedelta(days=5)).isoformat(),
        "owner_name": "Clarke Griffin",
        "owner_email": "clarke.griffin@test.com",
    }

    trips_repository.create_trip(trip_info)


@pytest.mark.skip(reason="Database interaction to find a trip")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trip = trips_repository.find_trip_by_id(trip_id)
    print()
    print(trip)


@pytest.mark.skip(reason="Database interaction to update a trip")
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_repository.update_trip_status(trip_id)


@pytest.mark.skip(reason="Database interaction to delete a trip")
def test_delete_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_repository.delete_trip(trip_id)
