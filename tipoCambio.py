import requests
import xml.etree.ElementTree as ET
import time

url = "https://www.banguat.gob.gt/variables/ws/tipocambio.asmx"
headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://www.banguat.gob.gt/variables/ws/TipoCambioDia"
    }
body = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <TipoCambioDia xmlns="http://www.banguat.gob.gt/variables/ws/" />
  </soap:Body>
</soap:Envelope>"""

# Returns today's rate of change
def tipoCambioHoy():
    max_retries = 5

    for attempt in range(max_retries):
        try:
            response = requests.post(url, data=body, headers=headers, timeout=10)
            response.raise_for_status()  # raise error for bad HTTP status

            root = ET.fromstring(response.text)

            namespaces = {
                'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
                'ns': 'http://www.banguat.gob.gt/variables/ws/'
            }

            referencia = root.find('.//ns:referencia', namespaces)

            if referencia is not None:
                rate = float(referencia.text)
                return rate
            else:
                raise ValueError("No se encontraron datos en la respuesta")

        except Exception as e:
            print(f"[Intento {attempt + 1}] Error: {e}")
            if attempt < max_retries - 1:
                sleep_time = 3 ** attempt
                print(f"Reintentando en {sleep_time} segundos...")
                time.sleep(sleep_time)
            else:
                print("Todos los intentos fallaron.")
                return None