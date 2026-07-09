# Channel Adaptation API - Centralized Advisory for Ethiopia

A minimal REST API prototype demonstrating the channel adaptation concept for the Digital Agriculture Advisory system.

## What is included

- `main.py`: FastAPI app with `GET /advisory` and `GET /health`
- `Dockerfile`: containerized API running on port `8000`
- `api-run-proof.txt`: captured build/run/test output showing successful responses
- `api-server-log.txt`: server startup log from the running container
- `Advisory Architecture.drawio.png`: exported `Question 2` architecture diagram

## Build

```bash
docker build -t advisory-api .
```

## Run

```bash
docker run -d -p 8000:8000 --name advisory-api advisory-api
```

## Test

```bash
# Weather advisory
curl "http://localhost:8000/advisory?region=Bahir%20Dar"

# Fertilizer advisory
curl "http://localhost:8000/advisory?region=Oromia"

# With region and farmer_id
curl "http://localhost:8000/advisory?region=Hawassa&farmer_id=FARM001"

# Lookup by farmer_id only
curl "http://localhost:8000/advisory?farmer_id=FARM001"

# Unknown region
curl "http://localhost:8000/advisory?region=Unknown"

# Health check
curl "http://localhost:8000/health"
```

### Example response

```json
{
  "region": "Bahir Dar",
  "type": "weather",
  "message": "Rain expected in 2 days. Delay fertilizer application.",
  "confidence": "medium"
}
```

### Error response

```json
{
  "detail": "No advisory available for region 'Unknown'. Supported regions: Bahir Dar, Oromia, Hawassa"
}
```

## How this plugs into the architecture

This API represents the Central Advisory Knowledge Base plus the Channel Adaptation Layer from the Question 2 architecture. A single endpoint returns advisory content that downstream SMS, IVR, and video formatting services could consume and transform into channel-specific outputs based on farmer profile routing.

## Evidence the API runs successfully

- `api-run-proof.txt` includes the exact Docker commands, container status, and captured `curl` responses.
- `api-server-log.txt` includes the Uvicorn startup log from the running container.

## Question 2 diagram artifact

- Exported diagram: `Advisory Architecture.drawio.png`
- Supporting editable/source notes: `architecture.md`

## Stop the container

```bash
docker stop advisory-api
docker rm advisory-api
```
