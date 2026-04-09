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

'''
#Funktion um nur ERROR's auszulesen
def error_only(log):
    return log["level"] == "ERROR"
'''

#Lesen des Log's Zeile für Zeile
with open("app.log", "r") as file:
    for line in file:
        log = parse_line(line)
        if log:
            print(log)

