from sqlalchemy import text
from src.database.connection import engine


def create_table():

    query = """
    CREATE TABLE IF NOT EXISTS earthquakes (
        event_id TEXT PRIMARY KEY,
        magnitude DOUBLE PRECISION,
        place TEXT,
        event_time TIMESTAMPTZ,
        updated_at TIMESTAMPTZ,
        event_url TEXT,
        longitude DOUBLE PRECISION,
        latitude DOUBLE PRECISION,
        depth DOUBLE PRECISION
    );
    """

    with engine.begin() as connection:
        connection.execute(text(query))


if __name__ == "__main__":
    create_table()
    print("Tabela earthquakes criada com sucesso!")