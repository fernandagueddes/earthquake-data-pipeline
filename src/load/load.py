
from sqlalchemy import MetaData, Table
from sqlalchemy.dialects.postgresql import insert as pg_insert

from src.extract.extract import extract_data
from src.transformation.transformation import transform_data
from src.database.connection import engine


def load_data(df):

    if df.empty:
        print("Nenhum dado para carregar.")
        return

    metadata = MetaData()

    earthquakes = Table(
        "earthquakes",
        metadata,
        autoload_with=engine
    )

    records = df.to_dict(orient="records")

    query = pg_insert(earthquakes).values(records)

    update_columns = {
        column.name: getattr(query.excluded, column.name)
        for column in earthquakes.columns
        if column.name != "event_id"
    }

    query = query.on_conflict_do_update(
        index_elements=["event_id"],
        set_=update_columns
    )

    with engine.begin() as connection:
        connection.execute(query)

    print(f"{len(records)} registros processados com sucesso!")


def run_pipeline():

    data = extract_data()

    df = transform_data(data)

    load_data(df)

    print("Pipeline executado com sucesso!")


if __name__ == "__main__":
    run_pipeline()

