# WALL-E — GitHub Project Review

## The Ecosystem Is Already Here

The "physical Muse" concept is not hypothetical — dozens of projects are already building pieces of it. The most important discovery: **the OS layer already exists**.

## Tier 1: Directly Relevant

| Project | Stars | What It Proves |
|---------|-------|---------------|
| **autonomous-ai/autonomous-os** | active | OS for physical AI agents. 24 skills, SOUL/DEVICE/SAFETY files. Runs on Reachy Mini, Unitree Go2. **This is the software layer we need.** |
| **broml/Project_Emily** | active | ESP32-S3 sentient robot: vision + voice + personality via Venice.ai. Three-unit architecture. **Closest to "physical Muse" — full companion.** |
| **clawsouls/clawsouls** | 19 | SoulSpec v0.5 — open-spec AI persona with embodied agent extensions. **The persona standard.** |
| **YonderZenith/AXIOM-Body** | — | Modular body system: eyes, ears, voice, face. File-based IPC, any LLM. **Agent → physical body bridge.** |
| **infinition/beee** | — | MCP-controlled face on ESP32-S3 touch screen. Agent shows emotions, asks approval. **MCP → physical face.** |

## Tier 2: ESP32 Companion Robots (Build Today)

| Project | Stars | BOM | What It Proves |
|---------|-------|-----|---------------|
| **Ksirailway-base/EVA-Robot** | 1 | Yes | Local AI companion: Whisper + Qwen + F5-TTS + OLED + camera. **End-to-end offline.** |
| **Amrit-R-M/EMO---Robot** | — | $30 | Voice-interactive, Groq Llama 3.1, personality modes. **Sub-2s response.** |
| **baryhuang/yuki-desktop-robot** | — | Yes | M5Stack StackChan, face tracking, curiosity engine. **M5Stack ecosystem proven.** |
| **SeanChangX/QBIT** | 88 | — | Community animation library, HA MQTT. **Social robot concept.** |

## Tier 3: Expression & Personality

| Project | Stars | What It Proves |
|---------|-------|---------------|
| **playfultechnology/esp32-eyes** | 200+ | Animated eyes, 18 emotions, auto-blink. **Reference for eye rendering.** |
| **karthick965938/robot-face-animations** | — | Board-agnostic face animations. **Drop-in library.** |
| **umersanii/SANGI** | 0 | 18 emotions, neglect/mood drift. **Attention-arc personality.** |
| **Rayan7717/Focus_Bot** | 8 | 10 emotions, 18 animations, circadian rhythm. **Personality evolves.** |
| **Maestro8484/IRIS** | — | Gaze-tracking eyes, streaming LLM speech, tripartite affect. **Most expressive face.** |

## Tier 4: Embodiment Frameworks

| Project | Stars | What It Proves |
|---------|-------|---------------|
| **oliviazzzu/minimal-embodiment** | 216 | LLM with closed-loop physical self-perception. **Academic validation.** |
| **rockywuest/pidog-embodiment** | — | Brain/Body architecture, 10 emotions, autonomous behaviors. **Multi-body support.** |
| **webdevtodayjason/hermes-embodiment** | — | Agent state → physical face + LEDs + voice. **Real-time embodiment.** |
| **lifemate-ai/embodied-gemini** | 3 | MCP-based body: eyes, ears, voice, legs. **Gemini → physical.** |
| **kamalkantsingh10/OLAF** | — | Personality-first robotics, 5 modules, OnShape CAD. **Modular expression.** |

## Tier 5: 3D Printable Robot Bodies

| Project | Stars | What It Proves |
|---------|-------|---------------|
| **MK040412/AlohaMini** | — | Complete robot: STL + STEP + BOM + firmware. **Full open-source stack.** |
| **g-ch/anything2robot** | — | Text/image → 3D mesh → URDF. **Generative robot body.** |
| **lhm0/marvin_robot** | — | 3D-printed ESP32 toy robot with all CAD + firmware. **Complete product.** |
| **plomek/Axon-Robot** | 44 | Full humanoid with OnShape CAD + Printables STL. **Production-ready CAD.** |

## Key Insight: autonomous-os is the missing piece

`autonomous-ai/autonomous-os` is essentially what we described as the "POW connector":

- SOUL files define personality
- DEVICE files define hardware capabilities
- SAFETY files define constraints
- SKILL files define behaviors
- Runs on Reachy Mini, Unitree Go2, custom ESP32 devices

This is exactly the software layer that makes "Muse designs itself" possible.

## Recommendation: Integrate, Don't Duplicate

1. **Use autonomous-os** as the personality/body OS
2. **Use clawsouls** as the persona standard
3. **Use esp32-eyes** for expression rendering
4. **POW provides**: hardware recipes, component validation, manufacturing routing
5. **The consumer sees**: Muse/personality → physical body → shipped product

The stack is converging naturally across 30+ open projects.
