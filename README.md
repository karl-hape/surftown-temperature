# Surftown Wassertemperatur

Automatische Erfassung der aktuellen Wassertemperatur der Surftown München sowie ergänzender lokaler Wetterdaten über die [Open-Meteo API](https://open-meteo.com/). Dieses Repository dient als öffentliches Daten-Backend für eine eigene Android-App.

## Automatisierung

Die Datenerfassung läuft über den GitHub-Actions-Workflow `.github/workflows/check_temp.yml`.

* **Auslöser:** Um Verzögerungen und Ausfälle der internen GitHub-Cron-Warteschlange zu vermeiden, wird der Workflow extern über **[cron-job.org](https://cron-job.org/)** per GitHub-API (`workflow_dispatch`) gestartet.
* **Intervall:** Alle 6 Stunden um **00:26, 06:26, 12:26 und 18:26 Uhr** (`Europe/Berlin`, inkl. automatischer Sommer-/Winterzeitumstellung).
* **Fehlertoleranz:** Zeitüberschreitungen der Wetter-API werden abgefangen, sodass die Wassertemperatur dennoch zuverlässig protokolliert wird.

## Datenformat (`wassertemperatur.csv`)

Alle Messwerte werden semikolongetrennt in der Datei `wassertemperatur.csv` gespeichert:

```text
Datum Uhrzeit; Wassertemperatur °C; Lufttemperatur °C; Luftfeuchte %; Windstärke km/h; Windrichtung; WMO-Wettercode
```

**Direktlink zu den Rohdaten (Raw):**
`https://raw.githubusercontent.com/karl-hape/surftown-temperature/main/wassertemperatur.csv`

## Repository-Struktur

* `.github/workflows/check_temp.yml` – Workflow-Skript zum Abrufen und Speichern der Messwerte
* `wassertemperatur.csv` – Fortlaufend aktualisierte Messdaten