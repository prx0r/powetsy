# V1 Strategy — Deliberately Constrained

## The Clean Wedge

> "You made a simple physical-agent design. Here's the cheapest credible way to make it real."

Objects: desk companions, plant devices, smart lamps, talking objects, pan/tilt cameras, sensor creatures, kids' toys, pet devices, simple rovers, ambient speakers, agent control surfaces.

Composition: compute + sensor + speaker/display/light + 0-2 servos + USB/battery + printed enclosure.

## Build Templates (10 to start)

VOICE_PUCK, DISPLAY_FACE, PAN_TILT_HEAD, PLANT_NODE, SMART_LAMP,
DESK_CONTROLLER, MOVING_CAMERA, MINI_ROVER, PET_DEVICE, SENSOR_BOX

Each knows: allowed electronics, dimensions, clearances, power, wiring,
mounting patterns, firmware, supplier alternatives.

## The MCP Interaction

Muse: "I want a body."
POW: "What capabilities?"
Muse: "voice, movement, lighting. Budget $50, qty 1."
POW: "Here's the implementation route with cost/timeline/confidence."

## Three Routes Per Request

```text
                 COST     LEAD TIME     INTEGRATION     CONFIDENCE
Branded modules  $31      5–8 days      very low        96%
China modules    $17      10–18 days    medium          82%
Custom PCBA      $9@100   15–25 days    upfront work    91%
```

## Key Primitive: resolve_capability()

Returns 3-5 viable implementation routes, not 700 listings.

## Proprietary Fields

usage_evidence, substitution_confidence, integration_effort,
landed_cost, lead_time, supply_risk, documentation_quality, observed_success

## The Progression

1 unit → modules
10 units → modules + batch fabrication
100 units → custom carrier PCB
1000 units → integrated PCB + optimized Chinese components

## V1 Scope: 100-200 Known-Good Primitives

20 compute, 30 sensors, 20 audio, 20 displays, 30 motors, 10 power, 5 fabrication routes.
Each extremely well understood. Enables dozens of Etsy-scale products.
