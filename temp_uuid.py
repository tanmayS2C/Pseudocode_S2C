"""
UUID Regular Expression (REGEX)
The regex below can be used to validate the format of UUIDs:

[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}    
"""

import uuid

# Generate a UUID
original_uuid = uuid.uuid4()

# Convert UUID to a string without hyphens and in lowercase
uuid_string = str(original_uuid).replace("-", "").replace("e", "z")

# Convert the modified string back to the original UUID format
restored_uuid = uuid.UUID(uuid_string.replace("z", "e"))

print("Original UUID:", original_uuid)
print("Modified UUID String:", uuid_string)
print("Restored UUID:", restored_uuid)