
import objectbox
from datetime import datetime
from typing import Dict, Any

#Database model for user settings
@objectbox.Entity
class UserSettings:
    id = objectbox.Id()
    user_id = objectbox.String()
    settings: Dict[str, Any]
    last_update = objectbox.Date()
    last_activity = objectbox.Date()

# Handlers for Database operations
def save_user_setting(user_id: str, settings: Dict[str, Any], store: objectbox.Store):
    box = objectbox.Box(store, UserSettings)
    last_update = int(datetime.now().timestamp() * 1000)
    setting_entity = UserSettings(user_id, settings, last_update)
    box.put(setting_entity)

def get_user_setting(user_id: str, store: objectbox.Store) -> Dict[str, Any]:
    box = objectbox.Box(store, UserSettings)
    # Query logic to find settings by user_id
    query = box.query(UserSettings.user_id == user_id).build()
    result = query.find()
    
    if result:
        return eval(result[0].settings_json) # Parse back the dictionary
    return {}