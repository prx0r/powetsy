# Botsi — "Printify for Consumer Robotics / Physical Agents"

**"Printify for consumer robotics / physical agents" is already technically possible in pieces.** What does not yet appear to exist as a polished commodity platform is the full workflow:

> choose a known-good core → customize enclosure/peripherals/software → order 1–5 → validate → automatically graduate to 50/500 → optionally fulfil directly to customers.

That gap is substantially more interesting than building another robot brand.

## The UX

```text
START WITH A CORE

Agent Mini    $12-ish    ESP32-S3, Wi-Fi/BLE, mic, USB-C, GPIO
Agent Vision  camera, mic, Wi-Fi, local lightweight vision
Agent Linux   Pi / Rockchip / N100-class, camera, audio, USB
Agent Motion  controller, servo/motor outputs, encoders, CAN
```

Then customize:

```text
"I want a little plant creature."

ADD: soil moisture, light, temperature, speaker, eyes, servo, RGB glow

CUSTOMIZE: body/character, 3D geometry, colour, voice, personality, branding, packaging
```

Then receive:

```text
1 UNIT    printed enclosure, commodity modules, hand assembled     $X
10 UNITS  same architecture, batch printed                         $Y/unit
100 UNITS custom carrier PCB, batch assembly                       $Z/unit
1000 UNITS integrated PCB, molded enclosure, optimized components  $W/unit
```

## The key insight: don't force custom PCB at first

Start from known modules. Only collapse into custom board once demand validates.

## Build Recipe — the canonical object

```text
BUILD RECIPE

purpose / intent
capabilities

architecture / parts / interfaces

software / firmware

geometry / CAD

assembly / tests

suppliers / manufacturing processes

cost @ quantities

alternatives / substitutions

provenance / known failures

version
```

A product is a versioned recipe. A robot is a complicated recipe. A smart lamp is a recipe.

## Three business models

1. **Affiliate/Refer** — POW says buy these exact parts
2. **Kit** — Bundle parts and ship together
3. **Private Label** — Demand proven → custom board/enclosure

## Key suppliers

Makerfabs: 1-piece prototyping through batch, drop-shipping
Seeed: Co-Create program, manufacturing + marketing + distribution
Elecrow: 1-piece PCBA, turnkey sourcing
M5Stack: modular ESP32 ecosystem, custom projects
XCM: MOQ 1 CNC parts

## The data garden

Collect known-good recipes from 10,000+ projects (GitHub, Hackaday, OSHWA, ESPHome, etc.).

Discover:

```text
camera A + board B + servo C
appears together in 417 successful projects
```

vs:

```text
camera X + board Y
appears in 3, has 11 driver issues
```

Physical-design agent gets **prior evidence**.

## API-first positioning

```text
pow.resolve({
  capability: "interactive desk companion",
  target_cost: 25,
  qty: 20,
  requirements: ["hear", "speak", "move_head", "rgb", "wifi"]
})
```

Returns recipe + cost estimates + assembly routing + evidence + risks.

## The endgame

> Printify lets anyone create a clothing brand without owning a garment factory. POW could eventually let agents/creators create physical-agent brands without understanding electronics factories.
