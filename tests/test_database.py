from sqlalchemy import text

from app.database import engine, SessionLocal


def test_database_connection():

    assert engine is not None
    assert SessionLocal is not None

    db = SessionLocal()

    try:
        result = db.execute(text("SELECT 1"))
        assert result.scalar() == 1

    finally:
        db.close()