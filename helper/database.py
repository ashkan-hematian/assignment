import os
from typing import Any, Hashable, Never
from pymongo import MongoClient, errors
from pymongo.database import Database


class DatabaseManager:
    client: MongoClient[Never]
    db: Database[Any]

    def __init__(self) -> None:
        is_debugging_str = os.getenv('DEBUG', 'False')
        is_debugging: bool = is_debugging_str.lower() in ['true']
        try:
            if is_debugging:
                self.client = MongoClient('mongodb://localhost:27017/')
            else:
                self.client = MongoClient('mongodb://mongo:27017/')
            self.db = self.client["assignment"]
            print("Connected to MongoDB and accessed database successfully.")
        except errors.ConnectionFailure as e:
            # Handle connection failures
            print(f"Could not connect to MongoDB: {e}")
        except errors.ConfigurationError as e:
            # Handle configuration errors
            print(f"Configuration error: {e}")
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")

    def is_connected(self) -> bool:
        return self.client is not None and self.db is not None

    def disconnect(self) -> None:
        if self.client:
            self.client.close()

    def insertMany(self, documents: list[dict[Hashable, Any]], collection_name: str) -> Any:
        if not self.is_connected():
            raise RuntimeError("Not connected to MongoDB")

        collection = self.db[collection_name]
        try:
            insert_result = collection.insert_many(documents)
            return insert_result.inserted_ids
        except Exception as e:
            raise e
