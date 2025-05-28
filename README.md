# Astrynn DevForge

_Módulo Python y OpenAI Plugin para calcular liability en apuestas lay con ajustes avanzados._

## Instalación

```bash
pip install .
from betynic.utils import calc_liability

# Liability por defecto (5% comisión):
liab = calc_liability(stake=100, lay_odds=3.0)
print(liab)  # ≈10.0

# Con comisión personalizada:
liab2 = calc_liability(50, 4.0, commission_rate=0.07)
POST /liability/
{ "stake": 100, "lay_odds": 3.0 }
1. **Debajo** de la sección de Instalación pones la línea `---` (o un simple salto de línea) y a continuación la cabecera `## Uso básico`.  
2. Tras el bloque de “Uso básico” repites el patrón (`---` + `## Endpoints (próximamente)` + contenido).  
3. Finalmente, al final del README pones la sección `## Licencia`.

Con esa estructura tu `README.md` quedará perfectamente ordenado y legible.
