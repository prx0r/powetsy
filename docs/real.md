# Real — Grounded Positioning

> **POW should not manufacture robots. POW should normalize the fragmented Chinese physical-AI supply chain into something agents can query and transact with.**

## What Already Exists

Shenzhen firms manually doing pieces of this:

- **Fdata**: configurable robot platforms + OEM/ODM, open APIs, ROS support
- **Wellwit**: modular robot platforms for integrators to build branded variants
- **Videostrong**: companion-robot, smart-speaker, elderly-care ODM with third-party AI/cloud
- **Aixumo/Navoltech**: sourcing companies bridging foreign teams into Shenzhen manufacturers

What's missing: the normalized programmable layer.

## Three APIs

### 1. search
```text
search_platforms({
    capabilities: ["camera", "microphone", "speaker", "pan_tilt"],
    max_unit_cost: 40,
    prototype_qty: 1,
    eventual_qty: 500
})
```

### 2. quote
```text
quote({
    base_platform: "...",
    quantity: 10,
    customization: { enclosure: "custom", firmware: true, branding: true }
})
```

### 3. order
```text
order(build_id, quantity=10)
```

## The Capability Primitive

Normalize what suppliers can instantiate, not their categories.

```text
hear, speak, see, video_call, display, wifi, cloud_agent
move, navigate, carry, slam, ros, sensor_integration
```

## Multi-Level Routing

> "desktop body with voice, camera, movement under $70"

```text
ROUTE A — existing ODM product, modify firmware + shell    $48
ROUTE B — standard modules, M5/Seeed + printed enclosure  $36
ROUTE C — custom PCBA                                    $29 @ 100
ROUTE D — existing companion robot white-label            $41 min 20
```

## The Moat: Manufacturing Outcome Graph

Not scraping Alibaba. Accumulating:

```text
supplier_claimed_moq: 100 → actual: 20
claimed_sample_time: 14d → observed: 27d
unit_price@100: $32 → $500: $21 → $1000: $17
POW builds completed: 14, on_time: 79%, defect_rate: 1.8%
```

## Bootstrap: 30-50 Suppliers, Same 5-10 Projects

Give every supplier the same canonical builds. Get apples-to-apples quotes.

Then repeat quarterly → **Chinese Physical-AI Manufacturing Cost Index**.

## The Endgame

Customer gives capability contract. POW knows implementations. If supply changes, POW substitutes. The abstraction becomes the product.

## Two Projects

**powphysical** — the garden (suppliers, platforms, prices, outcomes)
**powroute** — the transaction/compiler layer (intent → build → reorder)
