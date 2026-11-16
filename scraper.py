from datetime import datetime
from playwright.sync_api import sync_playwright

def get_water_temp():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Normalen Browser vortäuschen, um Bot-Abwehr zu umgehen
        page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        page.goto("https://surftown.de", wait_until="domcontentloaded")

        try:
            # Aktiv auf das Element warten (max 15 Sekunden)
            element = page.locator(".surftown-opening-infos--water-temperature")
            element.wait_for(state="visible", timeout=15000)
            temp = element.inner_text()
            
            # Formatierung bereinigen: "9° C" -> "9"
            temp = temp.replace("°", "").replace("C", "").strip()
        except Exception as e:
            # Den genauen Fehler ins GitHub-Log schreiben
            print(f"Detail-Fehler: {e}")
            temp = "Fehler beim Auslesen"

        browser.close()
        return temp

if __name__ == "__main__":
    temperatur = get_water_temp()
    zeitstempel = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("wassertemperatur.txt", "a", encoding="utf-8") as f:
        f.write(f"{zeitstempel} - {temperatur}\n")
    
    print(f"Abgeschlossen mit Wert: {temperatur}")
