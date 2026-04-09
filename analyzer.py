#Log Analyzer in python... Auswertung von INFO, WARNING oder FEHLER - Meldungen

#Erzeugen von eigenen Log's für Tests
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logging.info("App gestartet")
logging.error("Fehler aufgetreten")
logging.warning("Achtung!")

def parse_line(line):
    parts = line.split(" ", 3)

    if len(parts) < 4:
        return None  # ungültige Zeile ignorieren

    return {
        "timestamp": parts[0] + " " + parts[1],
        "level": parts[2],
        "message": parts[3].strip()
    }

request = input("INFO, WARNING, ERROR oder Alles?: ")

#Lesen des Log's Zeile für Zeile
with open("app.log", "r") as file:
    for line in file:
        log = parse_line(line)

        if not log:
            continue

        if request.lower() == "error":
            if log["level"] == "ERROR":
                print(log)
        
        if request.lower() == "info":
            if log["level"] == "INFO":
                print(log)

        if request.lower() == "warning":
            if log["level"] == "WARNING":
                print(log)
        
        if request.lower() == "alles":
            print(log)
