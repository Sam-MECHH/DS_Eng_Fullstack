"""
API de prédiction du prix de location - Projet Getaround.

Cette API expose un point de terminaison /predict qui renvoie le prix
de location journalier suggéré pour un véhicule, à partir de ses
caractéristiques.
"""

from typing import List, Union

import mlflow
import mlflow.sklearn
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import botocore

# ---------------------------------------------------------------------------
# Configuration de l'application
# ---------------------------------------------------------------------------
APP_TITLE = "API Getaround - Prédiction du prix de location"
APP_DESCRIPTION = (
    "Cette API met à disposition un modèle de Machine Learning entraîné (XGBoost Regressor) "
    "pour suggérer le prix journalier optimal d'une location de véhicule sur la plateforme Getaround.\n\n"
)
APP_VERSION = "1.0.0"

MLFLOW_TRACKING_URI = "https://sammec-mlflow-server-demo.hf.space"
MODEL_NAME = "getaround_model"
MODEL_URI = f"models:/{MODEL_NAME}@prod"

FEATURE_COLUMNS = [
    "model_key", "mileage", "engine_power", "fuel", "paint_color",
    "car_type", "private_parking_available", "has_gps",
    "has_air_conditioning", "automatic_car", "has_getaround_connect",
    "has_speed_regulator", "winter_tires",
]

BOOL_COLUMNS = [
    "private_parking_available", "has_gps", "has_air_conditioning",
    "automatic_car", "has_getaround_connect", "has_speed_regulator",
    "winter_tires",
]


# ---------------------------------------------------------------------------
# Initialisation
# ---------------------------------------------------------------------------
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

# Chargement du modèle
try:
    # Depuis Mlflow
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    model = mlflow.sklearn.load_model(MODEL_URI)
    MODEL_LOADED = True
except Exception as exc:
    print(f"Erreur de chargement du modèle : {exc}")
    model = None
    MODEL_LOADED = False


# ---------------------------------------------------------------------------
# Schémas Pydantic
# ---------------------------------------------------------------------------
class PredictionInput(BaseModel):
    """Schéma d'entrée pour l'endpoint /predict."""

    input: List[List[Union[str, int, float, bool]]] = Field(
        ...,
        examples=[[[
            "Citroën", 140411, 100, "diesel", "black", "convertible",
            True, True, False, False, True, True, True,
        ]]],
    )


class PredictionOutput(BaseModel):
    """Schéma de sortie pour l'endpoint /predict."""

    prediction: List[float]


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------
@app.get("/", tags=["Accueil"])
async def root():
    """Point d'entrée par défaut."""
    return {
        "message": "API Getaround opérationnelle",
        "version": APP_VERSION,
        "model_loaded": MODEL_LOADED,
        "documentation": "/docs",
    }


@app.get("/health", tags=["Accueil"])
async def health():
    """Indicateur de santé du service."""
    return {"status": "ok" if MODEL_LOADED else "model_missing"}


@app.post(
    "/predict",
    tags=["Prédiction"],
    response_model=PredictionOutput,
    summary="Prédire le prix de location journalier",
)
async def predict(payload: PredictionInput):
    """Renvoie la prédiction du prix de location journalier (EUR/jour)."""
    if not MODEL_LOADED:
        raise HTTPException(
            status_code=503,
            detail="Modèle non chargé sur le serveur.",
        )
    try:
        df_input = pd.DataFrame(payload.input, columns=FEATURE_COLUMNS)

        # Conversion des types
        for col in BOOL_COLUMNS:
            df_input[col] = df_input[col].astype(int)
        df_input["mileage"] = df_input["mileage"].astype(int)
        df_input["engine_power"] = df_input["engine_power"].astype(int)

        preds = model.predict(df_input)
        return {"prediction": [round(float(p), 2) for p in preds]}
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=f"Erreur lors de la prédiction : {exc}",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=False)