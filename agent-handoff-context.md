# Digital Agriculture Advisory Recruitment Exercise - Agent Handoff

## Purpose

This file gives another agent the minimum complete context needed to continue work on the recruitment exercise in `C:\Users\hp\ALL_PROJECTS\PXD` without re-reading the full conversation.

## Working Folder

- Project folder: `C:\Users\hp\ALL_PROJECTS\PXD`
- Existing source reference: `Digital Agriculture Advisory Based Recruitment Exercise.pdf`
- Completed spreadsheet for Question 1: `farmer-profiling-q1.xlsx`

## Assignment Summary

The PDF is a 3-part recruitment exercise for a digital agriculture advisory system.

### Question 1

Create a spreadsheet that profiles 10 farmers and recommends the best advisory delivery channel for each:

- `SMS`
- `IVR`
- `Video`
- or a combination

Each farmer also needs one sentence of reasoning.

Status:
- Completed.
- Deliverable already created as `farmer-profiling-q1.xlsx`.

### Question 2

Create a simple architecture diagram for `Centralized Advisory for Ethiopia`.

The diagram must show:

- one place where both advisory types are authored/generated once
- AI specifically for the weather advisory
- fertilizer advisory as more rule-based/static logic
- a channel adaptation layer that converts a single advisory into:
  - `SMS`
  - `IVR`
  - `Video`
- where farmer profiling determines which channel(s) each farmer receives
- one realistic external dependency such as:
  - weather forecast API/model
  - text-to-speech engine
  - video hosting/streaming service

It also needs a written explanation paragraph of `5 to 8 sentences` covering:

- one assumption about data flow
- one risk or limitation
- one question for the technical/dev team

Status:
- Planning complete.
- We now have `draw.io MCP` connected in Codex and can generate the diagram directly.

### Question 3

Build a small REST API prototype representing the channel adaptation concept.

Requirements from the PDF:

1. Build one simple REST API endpoint using any free open-source framework such as:
   - Python `Flask` or `FastAPI`
   - Node.js `Express`
2. Endpoint accepts `farmer_id` or `region`, for example:
   - `GET /advisory?region=Bahir%20Dar`
3. Return mock advisory JSON.
4. Hardcode at least `2 to 3` sample responses, including:
   - one weather advisory
   - one fertilizer advisory
5. No real weather API integration is required.
6. Containerize the API using Docker.
7. Include a `Dockerfile`.
8. Include a short `README` describing:
   - exact build command
   - exact run command
   - how the API was tested
   - one sentence explaining how this API plugs into the Question 2 channel adaptation layer

Expected example response shape:

```json
{
  "region": "Bahir Dar",
  "type": "weather",
  "message": "Rain expected in 2 days. Delay fertilizer application.",
  "confidence": "medium"
}
```

## Background Context From The PDF

The system produces two types of agricultural content:

1. `AI-based weather advisory`
   - short-term forecast translated into practical planting/irrigation/fertilizer guidance
2. `Fertilizer advisory`
   - recommendation on what to apply, how much, and when
   - based on crop stage and soil/region data

The business problem is that this content must reach farmers through:

- `IVR`
- `SMS`
- `Video`

without the content team recreating the same advisory separately for each channel.

Farmer device groups in the PDF:

- Group A: personal Android smartphone
- Group B: personal feature phone
- Group C: no personal phone or shared feature phone access

## Completed Question 1 Logic

These are the approved recommendation patterns already used in the spreadsheet:

- Personal smartphone + literate + good data -> `Video + SMS`
- Personal feature phone + literate -> `SMS`
- Low literacy or cannot read SMS -> `IVR`
- Smartphone but low literacy -> `IVR + Video`
- Shared phone access often justifies a combination channel
- Poor network reduces confidence in `Video`
- Voice preference supports `IVR`

Question 1 is considered done unless a shared Google Sheet link is explicitly required.

## Question 2 Draft Architecture

This is the planned structure for the architecture diagram.

### Core Components

1. `Weather Forecast API / Model`
2. `Weather Advisory AI Engine`
3. `Fertilizer Rules / Agronomy Logic`
4. `Central Advisory Knowledge Base`
5. `Channel Adaptation Layer`
6. `SMS Formatter`
7. `IVR Script Generator + TTS`
8. `Video Script / Storyboard Generator`
9. `Farmer Profile Database`
10. `Channel Routing / Delivery Decision`
11. `SMS Gateway`
12. `IVR Platform`
13. `Video Hosting / Delivery`
14. `Farmers`

### Intended Flow

- `Weather Forecast API / Model` -> `Weather Advisory AI Engine`
- `Weather Advisory AI Engine` -> `Central Advisory Knowledge Base`
- `Fertilizer Rules / Agronomy Logic` -> `Central Advisory Knowledge Base`
- `Central Advisory Knowledge Base` -> `Channel Adaptation Layer`
- `Channel Adaptation Layer` -> `SMS Formatter`
- `Channel Adaptation Layer` -> `IVR Script Generator + TTS`
- `Channel Adaptation Layer` -> `Video Script / Storyboard Generator`
- `Farmer Profile Database` -> `Channel Routing / Delivery Decision`
- `SMS Formatter` -> `Channel Routing / Delivery Decision`
- `IVR Script Generator + TTS` -> `Channel Routing / Delivery Decision`
- `Video Script / Storyboard Generator` -> `Channel Routing / Delivery Decision`
- `Channel Routing / Delivery Decision` -> `SMS Gateway`
- `Channel Routing / Delivery Decision` -> `IVR Platform`
- `Channel Routing / Delivery Decision` -> `Video Hosting / Delivery`
- `SMS Gateway` -> `Farmers`
- `IVR Platform` -> `Farmers`
- `Video Hosting / Delivery` -> `Farmers`

### Draft Explanation Paragraph

Use or refine this:

> My main assumption is that both weather and fertilizer advisories can be stored in a single structured knowledge base before being converted into channel-specific formats. In this design, the AI component is used only for the weather advisory, where forecast data is translated into farmer-friendly recommendations, while fertilizer advice is generated from more stable agronomic rules. The channel adaptation layer prevents the content team from rewriting the same message separately for SMS, IVR, and video. Farmer profile data then determines whether a farmer receives text, voice, video, or a combination based on device access, literacy, and connectivity. One realistic external dependency is a weather forecast API or model, since the weather advisory depends on timely forecast inputs. A key risk in this design is that inaccurate forecasts or weak connectivity could reduce the usefulness of the final advisory for some farmers. Before finalizing the system, I would ask the technical team how farmer profiles are updated over time so channel decisions stay accurate when device access or network conditions change.

## draw.io Status

`draw.io MCP` is now connected and available in this Codex environment.

Available relevant tools include:

- `mcp__drawio.open_drawio_mermaid`
- `mcp__drawio.open_drawio_xml`

So another agent can generate the diagram directly instead of only describing it.

## Recommended Next Step For A Coding Agent

If the goal is to continue toward implementation, start with `Question 3`.

Recommended stack:

- `Python FastAPI`

Reason:

- very small amount of code
- easy JSON response handling
- simple Dockerization
- easy README and curl testing

Suggested project structure:

- `main.py`
- `requirements.txt`
- `Dockerfile`
- `README.md`

Suggested endpoint:

- `GET /advisory`

Suggested query parameters:

- `region`
- optional `farmer_id`

Suggested behavior:

- return weather advisory for one region
- return fertilizer advisory for another region
- return a fallback advisory if no exact match exists

Example sample data:

```json
[
  {
    "region": "Bahir Dar",
    "type": "weather",
    "message": "Rain expected in 2 days. Delay fertilizer application.",
    "confidence": "medium"
  },
  {
    "region": "Oromia",
    "type": "fertilizer",
    "message": "Apply urea at the early vegetative stage in the recommended dosage for your area.",
    "confidence": "high"
  },
  {
    "region": "Hawassa",
    "type": "weather",
    "message": "Dry conditions are expected this week. Prepare irrigation if available.",
    "confidence": "medium"
  }
]
```

## Constraints And Expectations

- Keep the implementation intentionally small.
- No real external API integration needed.
- Mock data is acceptable and expected.
- Docker must run the API on an exposed port such as `5000` or `8000`.
- README should include exact commands, not vague instructions.
- This is a prototype demonstrating how a shared advisory source could feed downstream channel adaptation components.

## Deliverables Status Snapshot

- `Question 1`: complete
- `Question 2`: ready to generate in draw.io
- `Question 3`: not started
