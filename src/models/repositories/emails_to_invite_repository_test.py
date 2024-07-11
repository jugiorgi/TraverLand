import pytest
import uuid
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="Database interaction to register an email")
def test_register_email():
    conn = db_connection_handler.get_connection()
    email_repository = EmailsToInviteRepository(conn)

    email_info = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "clarke@test.com",
    }

    email_repository.register_email(email_info)


@pytest.mark.skip(reason="Database interaction to find an email by trip id")
def test_find_email_by_trip_id():
    conn = db_connection_handler.get_connection()
    email_repository = EmailsToInviteRepository(conn)

    emails = email_repository.find_email_by_trip_id(trip_id)
    print(emails)
