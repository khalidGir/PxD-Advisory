from fastapi import FastAPI, Query, HTTPException
from typing import Optional

app = FastAPI(
    title="Channel Adaptation API",
    description="Mock REST API for the Centralized Advisory for Ethiopia system",
    version="1.0.0",
)

ADVISORIES = {
    "bahir dar": {
        "region": "Bahir Dar",
        "type": "weather",
        "message": "Rain expected in 2 days. Delay fertilizer application.",
        "confidence": "medium",
    },
    "oromia": {
        "region": "Oromia",
        "type": "fertilizer",
        "message": "Apply urea at the early vegetative stage in the recommended dosage for your area.",
        "confidence": "high",
    },
    "hawassa": {
        "region": "Hawassa",
        "type": "weather",
        "message": "Dry conditions are expected this week. Prepare irrigation if available.",
        "confidence": "medium",
    },
}

FARMER_REGION_MAP = {
    "FARM001": "hawassa",
    "FARM002": "bahir dar",
    "FARM003": "oromia",
}


@app.get("/advisory")
def get_advisory(
    region: Optional[str] = Query(None, description="Region name (e.g. 'Bahir Dar')"),
    farmer_id: Optional[str] = Query(None, description="Optional farmer identifier"),
):
    if not region and not farmer_id:
        raise HTTPException(
            status_code=400,
            detail="Provide either region or farmer_id.",
        )

    key: Optional[str] = None
    if region:
        key = region.strip().lower()
    elif farmer_id:
        key = FARMER_REGION_MAP.get(farmer_id.upper())

    if key not in ADVISORIES:
        if farmer_id and not region:
            raise HTTPException(
                status_code=404,
                detail=f"No advisory available for farmer_id '{farmer_id}'. Supported farmer_ids: FARM001, FARM002, FARM003",
            )
        raise HTTPException(
            status_code=404,
            detail=f"No advisory available for region '{region}'. Supported regions: Bahir Dar, Oromia, Hawassa",
        )

    if farmer_id:
        result = dict(ADVISORIES[key])
        result["farmer_id"] = farmer_id
        return result
    return ADVISORIES[key]


@app.get("/health")
def health():
    return {"status": "ok"}
