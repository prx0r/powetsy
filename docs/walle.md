# WALL-E — Physical Muse

> **Muse designs the personality, appearance and behavior. POW constrains the body to manufacturable hardware.**

## The Product

User says: "Make a physical version of my Muse."

```text
create_physical_agent({
  budget: 80,
  capabilities: ["hear", "speak", "look_at_user", "ambient_light"],
  power: "usb_c",
  size: "desktop",
  manufacturing_qty: 1
})
```

POW provides a **capability palette** — already sourced, priced, dimensioned, electrically compatible, firmware-supported, tested.

Muse goes crazy on the **form**.

## Five Templates

1. **AMBIENT** — light + speaker + mic
2. **FACE** — display + mic + speaker
3. **HEAD** — face + pan/tilt
4. **CREATURE** — head + 2–4 small actuators
5. **ROVER** — camera + wheels + audio

Each template exposes a design envelope with fixed invariants.

## The Printify Analogy

> here is a validated physical-agent skeleton → make almost any body/character around it.

## Customization Layers

**Body:** shape, size, expression, surface, color
**Senses:** camera, mic, temp, touch, plant sensor, motion
**Expression:** screen, LEDs, speaker, mechanical eyes, movement
**Mobility:** none, rotating head, legs, wheels
**Environment:** desk, garden, kitchen, bedroom, workshop

## Pricing

```text
Muse Body                    £49
+ vision                     £8
+ pan/tilt                   £7
+ battery                    £9
+ environmental sensors     £4
Total                       £77
```

## The Four Moats

1. **SUPPLY GRAPH** — what can actually be built
2. **DESIGN GRAPH** — which parts/templates fit together
3. **DEMAND GRAPH** — what people/Muses choose to create
4. **OUTCOME GRAPH** — what ships, works, breaks, reorders

## V1: Ruthlessly Constrained

> Create a physical body for your AI agent.

One core. Two body templates. Microphone + speaker + RGB + optional display/camera. AI-generated enclosure.

Prove: Muse → MCP → design constraints → generated CAD → parts → fabrication → assembly → shipped physical agent.
