
import pandas as pd


def create_data(data):
    df = pd.json_normalize(data["features"])

    return df


def select_columns(df):

    columns = [
        "id",
        "properties.mag",
        "properties.place",
        "properties.time",
        "properties.updated",
        "properties.url",
        "geometry.coordinates"
    ]

    df = df[columns]

    return df


def normalize_datetime(df):

    datetime_columns = [
        "properties.time",
        "properties.updated"
    ]

    for column in datetime_columns:
        df[column] = pd.to_datetime(
            df[column],
            unit="ms",
            utc=True
        )

    return df


def normalize_coordinates(df):

    df[["longitude", "latitude", "depth"]] = pd.DataFrame(
        df["geometry.coordinates"].tolist(),
        index=df.index
    )

    df = df.drop(columns=["geometry.coordinates"])

    return df


def rename_columns(df):

    columns = {
        "id": "event_id",
        "properties.mag": "magnitude",
        "properties.place": "place",
        "properties.time": "event_time",
        "properties.updated": "updated_at",
        "properties.url": "event_url"
    }

    df = df.rename(columns=columns)

    return df


def transform_data(data):

    df = create_data(data)
    df = select_columns(df)
    df = normalize_datetime(df)
    df = normalize_coordinates(df)
    df = rename_columns(df)

    return df

