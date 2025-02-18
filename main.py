from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

# Modelo de entrada para análisis de expansión
class ExpansionRequest(BaseModel):
    country: str

# Modelo de entrada para estrategia de marketing
class MarketingRequest(BaseModel):
    project: str

# Modelo de entrada para simulación de negociaciones
class NegotiationRequest(BaseModel):
    partner_type: str

# Modelo de entrada para reportes
class ReportRequest(BaseModel):
    topic: str

# Endpoint: Análisis de Expansión
@app.post("/expansion")
def analyze_expansion(data: ExpansionRequest):
    return {
        "opportunities": f"Oportunidades en {data.country}: Alta demanda en retail y centros comerciales.",
        "challenges": f"Retos en {data.country}: Competencia fuerte y barreras legales.",
        "recommendations": f"Estrategia recomendada: Ingresar mediante alianzas con centros comerciales en {data.country}."
    }

# Endpoint: Generador de Estrategia de Marketing
@app.post("/marketing")
def generate_marketing_strategy(data: MarketingRequest):
    return {
        "target_audience": f"Público objetivo identificado para {data.project}: Clientes de alto poder adquisitivo.",
        "channels": "Recomendamos redes sociales, influencers y eventos físicos.",
        "action_plan": f"Plan de acción: Crear contenido de alto valor para posicionar {data.project} en el mercado."
    }

# Endpoint: Simulación de Negociaciones
@app.post("/negotiation")
def simulate_negotiation(data: NegotiationRequest):
    return {
        "key_points": f"Negociación con {data.partner_type}: Presentar retorno de inversión y ventajas estratégicas.",
        "counterarguments": "Posibles objeciones: Altos costos iniciales y necesidad de pruebas de éxito.",
        "closing_strategy": "Recomendamos ofrecer un período de prueba con métricas de conversión para cerrar la negociación."
    }

# Endpoint: Generación de Reportes Ejecutivos
@app.post("/report")
def generate_executive_report(data: ReportRequest):
    return {
        "summary": f"Reporte sobre {data.topic}: Evaluación de impacto y proyecciones futuras.",
        "key_metrics": "Métricas clave: Engagement, tráfico y ventas generadas.",
        "recommendations": "Acciones recomendadas: Optimizar presencia digital y mejorar la experiencia del cliente."
    }

# Ejecutar el servidor localmente o en Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Usa el puerto de Render o 10000 por defecto
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
