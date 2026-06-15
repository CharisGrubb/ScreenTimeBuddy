

from pymongo import MongoClient
import os


class MongoDBSettings:
    def __init__(self):
        self.MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        self.client = MongoClient(self.MONGO_URI)
        self.db = self.client["ScreenTimeBuddy"]
        self.settings_collection = self.db["user_settings"]

    def save_user_settings(self, user_id, settings_dict):
        """ Saves or completely overwrites a user's settings.
        """
        # Use update_one with upsert=True to create the document if it does not exist
        result = self.settings_collection.update_one(
            {"user_id": user_id},
            {"$set": {"settings": settings_dict}},
            upsert=True
        )
        return result.acknowledged


    def get_user_settings(self, user_id):
        """
        Retrieves a user's settings document.
        """
        user_doc = self.settings_collection.find_one({"user_id": user_id})
        if user_doc:
            return user_doc.get("settings", {})
        return None


    def update_single_setting(self, user_id, setting_key, setting_value):
        """
        Updates a single specific setting using dot notation without touching the rest.
        """
        result = self.settings_collection.update_one(
            {"user_id": user_id},
            {"$set": {f"settings.{setting_key}": setting_value}}
        )
        return result.modified_count > 0
