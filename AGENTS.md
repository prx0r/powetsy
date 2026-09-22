# AGENTS.md — POWEtsy

## Positioning

**"Give your AI a body, one capability at a time."**

Single-purpose physical AI agents with personality + sensors + one or two actuators.

## Kit Architecture

Three reusable hardware stacks:
- SENSE NODE (ESP32-S3, mic, camera/sensor ports, Wi-Fi, USB-C)
- EXPRESS NODE (speaker, LED/display, servo outputs)
- MOTION NODE (motor drivers, encoders, CAN, power monitoring)

Products = enclosure + peripherals + software + branding.

## Supply Chain

Makerfabs → Seeed → Elecrow → M5Stack for manufacturing.
Start with commodity modules + printed enclosure. Scale to custom PCB when demand validates.

## The Moat

Not the hardware. The intelligence layer:
- Which modules are cheap/reliable
- Which architectures recur
- Which configurations become products
- What fails and what works
- Cost history over time

## Rule

POW = physical capability/data infrastructure.
Tiny consumer brands = experiments/spinouts built from POW discoveries.
