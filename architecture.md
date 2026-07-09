# Question 2 - Centralized Advisory for Ethiopia: Architecture

Exported diagram artifact for submission:

- `Advisory Architecture.drawio.png`

## Mermaid Diagram Source

```mermaid
flowchart TB
    subgraph Input["Input Sources"]
        WF[Weather Forecast API/Model] --> WAI[Weather Advisory AI Engine]
        FR[Fertilizer Rules / Agronomy Logic]
    end

    subgraph Core["Core Advisory"]
        WAI --> CAKB[Central Advisory Knowledge Base]
        FR --> CAKB
    end

    subgraph Adaptation["Channel Adaptation Layer"]
        CAKB --> CAL[Channel Adaptation Layer]
        CAL --> SMSF[SMS Formatter]
        CAL --> IVRG[IVR Script Generator + TTS]
        CAL --> VSG[Video Script / Storyboard Generator]
    end

    subgraph Routing["Channel Routing"]
        FPD[Farmer Profile Database] --> CR[Channel Routing / Delivery Decision]
        SMSF --> CR
        IVRG --> CR
        VSG --> CR
    end

    subgraph Delivery["Delivery Channels"]
        CR --> SMSG[SMS Gateway]
        CR --> IVRP[IVR Platform]
        CR --> VHD[Video Hosting / Delivery]
    end

    subgraph Farmers["End Users"]
        SMSG --> F[Farmers]
        IVRP --> F
        VHD --> F
    end

    style WF fill:#e1f5fe,stroke:#01579b
    style FR fill:#e1f5fe,stroke:#01579b
    style WAI fill:#fff3e0,stroke:#e65100
    style CAKB fill:#f3e5f5,stroke:#4a148c
    style CAL fill:#e8f5e9,stroke:#1b5e20
    style FPD fill:#fff8e1,stroke:#f57f17
    style CR fill:#fce4ec,stroke:#c62828
    style F fill:#f5f5f5,stroke:#616161
```

## Explanation

My main assumption is that both weather and fertilizer advisories can be stored in a single structured knowledge base before being converted into channel-specific formats. In this design, the AI component is used only for the weather advisory, where forecast data is translated into farmer-friendly recommendations, while fertilizer advice is generated from more stable agronomic rules. The channel adaptation layer prevents the content team from rewriting the same message separately for SMS, IVR, and video. Farmer profile data then determines whether a farmer receives text, voice, video, or a combination based on device access, literacy, and connectivity. One realistic external dependency is a weather forecast API or model, since the weather advisory depends on timely forecast inputs. A key risk in this design is that inaccurate forecasts or weak connectivity could reduce the usefulness of the final advisory for some farmers. Before finalizing the system, I would ask the technical team how farmer profiles are updated over time so channel decisions stay accurate when device access or network conditions change.
