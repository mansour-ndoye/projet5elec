from app.database import engine, SessionLocal

def test_database_objects_exist():
    assert engine is not None
    assert SessionLocal is not None