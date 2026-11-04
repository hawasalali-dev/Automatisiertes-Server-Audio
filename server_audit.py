import csv
import json
from datetime import datetime
import shutil
import os

def filter_kritische_server(csv_datei: str) -> list[dict]:
    kritische_server = []
    try:
        with open(csv_datei, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                if (
                    row['Status'].strip().lower() == 'online'
                    and int(row['Patch_Level']) < 5
                ):
                    kritische_server.append({
                        'Hostname': row['Hostname'],
                        'IP': row['IP'],
                        'OS': row['OS'],
                        'Patch_Level': row['Patch_Level']
                    })
    except FileNotFoundError:
        print(f"Fehler: Die Datei {csv_datei} wurde nicht gefunden.")
    except Exception as e:
        print(f"Unerwarteter Fehler beim Lesen der CSV-Datei: {e}")
    return kritische_server

def erstelle_audit_report(kritische_server: list[dict], ausgabe_datei: str) -> None:
    try:
        with open('servers.csv', 'r', encoding='utf-8') as file:
            anzahl_gescannter_server = sum(1 for _ in file) - 1

        report = {
            'Scan-Datum': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Anzahl_gescannter_Server': anzahl_gescannter_server,
            'Kritische_Server': kritische_server
        }

        with open(ausgabe_datei, mode='w', encoding='utf-8') as file:
            json.dump(report, file, indent=4, ensure_ascii=False)
        print(f"Audit-Report erfolgreich erstellt: {ausgabe_datei}")
    except Exception as e:
        print(f"Fehler beim Erstellen des Audit-Reports: {e}")

def logge_audit(kritische_server: list[dict], log_datei: str) -> None:
    try:
        anzahl_kritisch = len(kritische_server)
        log_zeile = (
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"Audit abgeschlossen. {anzahl_kritisch} kritische Server gefunden.\n"
        )

        with open(log_datei, mode='a', encoding='utf-8') as file:
            file.write(log_zeile)
        print(f"Log-Eintrag erfolgreich hinzugefügt: {log_datei}")
    except Exception as e:
        print(f"Fehler beim Schreiben des Log-Eintrags: {e}")

def sichere_zertifikat(quell_datei: str, backup_ordner: str) -> None:
    try:
        os.makedirs(backup_ordner, exist_ok=True)
        shutil.copy2(quell_datei, os.path.join(backup_ordner, 'server.crt.bak'))
        print(f"Zertifikat erfolgreich gesichert: {os.path.join(backup_ordner, 'server.crt.bak')}")
    except FileNotFoundError:
        print(f"Fehler: Die Zertifikatsdatei {quell_datei} wurde nicht gefunden.")
    except Exception as e:
        print(f"Fehler beim Sichern des Zertifikats: {e}")

if __name__ == "__main__":
    csv_datei = "servers.csv"
    json_datei = "audit_report.json"
    log_datei = "audit_history.log"
    zertifikat_datei = "server.crt"
    backup_ordner = "Backup"

    print("Starte automatisiertes Server-Audit...")

    print("Schritt 1: CSV-Inventar wird eingelesen...")
    kritische_server = filter_kritische_server(csv_datei)

    print("Schritt 2: Audit-Report wird erstellt...")
    erstelle_audit_report(kritische_server, json_datei)

    print("Schritt 3: Logbuch wird aktualisiert...")
    logge_audit(kritische_server, log_datei)

    print("Schritt 4: Zertifikat wird gesichert...")
    sichere_zertifikat(zertifikat_datei, backup_ordner)

    print("Audit erfolgreich abgeschlossen!")
