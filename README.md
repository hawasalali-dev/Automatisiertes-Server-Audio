# Automatisiertes-Server-Audio

# Automatisiertes Server-Audit-System

**Ein Python-basiertes Tool zur Analyse von Server-Inventaren, Filterung kritischer Server und Generierung von Audit-Berichten.**

---

##  **Funktionen**

| Schritt | Funktion | Beschreibung |
|---------|----------|--------------|
| 1 | **CSV-Inventar einlesen** | Liest Serverdaten aus einer CSV-Datei ein (Trennzeichen: `;`). |
| 2 | **Kritische Server filtern** | Identifiziert Server mit Sicherheitslücken (`Patch_Level < 5` und `Status = Online`). |
| 3 | **JSON-Audit-Report** | Erstellt einen strukturierten Audit-Bericht mit Metadaten. |
| 4 | **Logbuch fortschreiben** | Fügt Audit-Ergebnisse einem zentralen Logbuch hinzu. |
| 5 | **Zertifikats-Backup** | Sichert SSL-Zertifikate im Binärmodus in einen Backup-Ordner. |

---

## **Projektstruktur**

