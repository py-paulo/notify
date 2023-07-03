SCHEMA_SLACK = {
    "type": "object",
    "properties": {
        "channel": {"type": "string"},
        "token": {"type": "string"}
    }
}

SCHEMA_TEAMS = {
    "type": "object",
    "properties": {
        "webhook-url": {"type": "string"}
    }
}
