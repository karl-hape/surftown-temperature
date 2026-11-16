from datetime import datetime
from playwright.sync_api import sync_playwright

def get_water_temp():
    with sync_playwright() as p:
        # Headless Chromium starten
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://surftown.de", wait_until="domcontentloaded")

        # 3 Sekunden warten, bis das JavaScript die Daten geladen hat
        page.wait_for_timeout(3000)

        # Gezielt die CSS-Klasse auslesen
        try:
            temp = page.locator(".surftown-opening-infos--water-temperature").inner_text(timeout=5000)
        except Exception:
            temp = "Fehler beim Auslesen"

        browser.close()
        return temp

if __name__ == "__main__":
    temperatur = get_water_temp()
    zeitstempel = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Wert an die wassertemperatur.txt anhängen
    with open("wassertemperatur.txt", "a", encoding="utf-8") as f:
        f.write(f"{zeitstempel} - {temperatur}\n")
    
    print(f"Erfolgreich ausgelesen: {temperatur}")
