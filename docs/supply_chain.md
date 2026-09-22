# Supply Chain & Manufacturing Routing

## The Gap

What does **not** exist cleanly is a single "AI hardware startup backend" that routes concept → known modules → custom electronics → enclosure → assembly → testing → packaging → fulfilment.

## Practical Suppliers

### Makerfabs (Shenzhen)
- Explicitly supports makers/startups from **1-piece prototyping** through small batches
- PCB design, PCB/PCBA, component sourcing, programming, testing, mechanical design, 3D printing, CNC, molding, final assembly, packaging, drop-shipping
- Coordinates local Shenzhen design houses/factories
- PCB production from 1–1,000 pieces

### Seeed Studio
- PCB/PCBA, mechanical customization, firmware, logo/packaging, OEM/ODM, distribution
- Some light software customization has no MOQ
- Deeper Jetson products: **8–24 week** development, ~500-unit MOQ
- Shenzhen Open Parts Library: 15,000+ commonly sourced parts
- PCBA possible from a **single populated board**

### Elecrow
- PCB, sourcing, PCBA, subassembly/kitting, tooling, injection-molded enclosures
- Lower-volume electronics turnkey

### M5Stack
- Modular ESP32/display/sensor/control hardware
- Custom-project service in Shenzhen
- Already makes exactly the hardware for cheap physical agents

## Manufacturing Decision Graph

```text
QTY 5
M5Stack module
printed enclosure
hand assembly

QTY 50
custom PCB
printed enclosure
Shenzhen assembly

QTY 500
integrated PCB
custom molded enclosure

QTY 5000
optimized Chinese parts
injection mold
automated assembly
```

## Supply Workflow

```text
POW concept
   ↓
existing module selection
   ↓
ESP32/M5Stack/Seeed prototype
   ↓
3D-printed enclosure
   ↓
5–20 pilot units
   ↓
Makerfabs / Elecrow
   ↓
custom PCB when demand validates
   ↓
assembled + programmed + tested
   ↓
custom packaging
   ↓
direct shipping / fulfilment
```

## Kit Architecture

Three reusable hardware stacks:

```text
SENSE NODE
ESP32-S3, mic, camera/sensor ports, Wi-Fi, USB-C

EXPRESS NODE
speaker, LED/display, servo outputs

MOTION NODE
motor drivers, encoders, CAN, power monitoring
```

Products are mainly different: enclosure + peripherals + software + branding.

## Three Business Models

1. **Affiliate/Refer** — POW says buy these exact parts
2. **Kit** — Bundle parts and ship together
3. **Private Label** — Demand proven → custom board/enclosure

## "Give your AI a body, one capability at a time"

```text
SEE KIT     → camera + pan/tilt → "give Muse eyes"
HEAR KIT    → mic array + speaker → "give Muse ears and a voice"
MOVE KIT    → servo/motor controller → "let Muse move something"
LIGHT KIT   → addressable LEDs → "let Muse control ambient state"
SENSE KIT   → temp/humidity/motion/light → "let Muse perceive the room"
PLANT KIT   → moisture + light + pump relay → "give Muse access to your plant"
DESK KIT    → buttons + knob + screen + RGB → "physical control surface"
POWER KIT   → smart plugs / energy meter → "let Muse observe power usage"
```

## Progression

```text
POW finds cheap capable hardware
→ package it as an agent capability
→ ship connector + recipes
→ observe usage/demand
→ discover recurring combinations
→ integrate them
→ create new physical product
```
