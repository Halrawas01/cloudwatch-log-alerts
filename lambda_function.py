def lambda_handler(event, context=None):
    log_events = [
        {"message": "INFO: Everything is fine"},
        {"message": "WARNING: Something odd"},
        {"message": "ERROR: Something went wrong!"},
    ]

    alerts = []
    for log in log_events:
        message = log["message"]
        if "ERROR" in message:
            alerts.append(message)

    for alert in alerts:
        print("ALERT:", alert)

    return {"alerts": alerts}

lambda_handler({})
