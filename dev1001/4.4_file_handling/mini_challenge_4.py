# Task: Read updated_config.json. Change the theme to "light" and add a new
#       key-value pair "font_size": 12. Write this modified data to a new
#       file user_prefs.json.

import json

with open("updated_config.json", 'w') as f:
    config_data = json.load(f) 

config_data["key-value pair"].append("font_size:12")
