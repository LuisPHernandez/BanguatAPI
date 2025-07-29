from datetime import datetime, timedelta
from tipoCambio import tipoCambioHoy
from guardarTiposDeCambio import guardarTiposDeCambio
from obtenerFecha import obtenerUltimaFecha

def run_periodically(interval_minutes=5):
    fecha_actual = obtenerUltimaFecha()
    if (fecha_actual != None):
        next_day = (fecha_actual + timedelta(days=1)).strftime("%d/%m/%Y")
    else:
        next_day = datetime.now().strftime("%d/%m/%Y")

    print(f"Buscando tasa para: {next_day}")
    rate = tipoCambioHoy()
    if rate is not None:
        guardarTiposDeCambio(next_day, rate)

if __name__ == "__main__":
    run_periodically()