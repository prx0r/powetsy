# POWEtsy — Vision

The strongest version is not "general-purpose home robot." It is:

> **single-purpose physical agents with personality + sensors + one or two actuators.**

That is much cheaper, easier to manufacture, easier to explain on Etsy/TikTok, and much easier to personalize.

## Categories

* **Plant agents:** moisture/light/temp sensing, watering control, grow-light control, plant "mood" light, plant-to-audio, camera timelapse, notifications, ChatGPT/Muse interpreting the plant state.
* **Desk agents:** physical button/knob/display for your personal agent, status light for tasks, push-to-talk, reminders, pomodoro, trading/coding agent indicators.
* **Pet agents:** treat dispenser, camera, sound playback, enrichment toys, feeding reminders, personalized pet voice/avatar.
* **Ambient home agents:** smart lamps, speakers, scent devices, displays, kinetic sculptures, weather/status objects.
* **Relationship/gift objects:** two linked lamps, long-distance touch objects, personalized message printers, voice-memory boxes.
* **Maker/collector robots:** tiny expressive heads, moving cameras, little desktop creatures, AI-controlled ornaments.
* **Wellness/routine objects:** hydration reminders, medication boxes, sleep/wake lighting, breathing lights, physical habit trackers.

## The key insight

Most of these do **not** require robotics in the humanoid sense. A "robot" can be:

```text
sensor
+ compute/network
+ AI
+ light/sound/display
+ tiny actuator
+ enclosure
```

That can be a £15–£40 BOM.

## Personalization is where Etsy fits

Etsy customers already understand paying extra for "made for me."

```text
name
voice
appearance
engraving
LED behavior
3D-printed enclosure
plant/pet type
agent personality
specific Muse/ChatGPT workflow
```

Instead of competing with Amazon on commodity electronics, the product becomes:

> "This physical AI object was made specifically for Sarah and her monstera."

## The plant niche

Minimum viable hardware:

```text
ESP32
soil moisture sensor
ambient light sensor
temperature/humidity
RGB LED
USB-C
optional small pump relay
3D printed enclosure
```

Software layer:

```text
sensor readings
↓
plant profile
↓
agent interpretation
↓
"Your monstera is drying faster than usual."
↓
notification / lighting / watering action
```

## The progression from data garden to products

```text
POW observes cheap primitives
        ↓
detect viable product configuration
        ↓
prototype with commodity modules
        ↓
sell 10–50 through Etsy
        ↓
observe actual demand/failures
        ↓
integrate repeated configuration
        ↓
custom PCB / enclosure
        ↓
spin out tiny brand
```

## Three reusable node boards

### POW Agent Node
```text
ESP32-S3, USB-C, Wi-Fi/BLE, mic, speaker output, RGB, I2C, GPIO,
servo output, sensor ports
```

### POW Motion Node
```text
CAN, 2–4 motors, encoders, current sensing, servo outputs
```

### POW Power Node
```text
battery, charging, DC/DC, BMS, power monitoring
```

Three primitives → many consumer physical-agent products.

## The continuum

```text
Today: ChatGPT/Muse lives in a phone
Next: it controls your lamp
Then: it has a microphone on your desk
Then: it sees through a camera
Then: it controls your plant watering
Then: it has a little pan/tilt head
Then: it has wheels
```

## The derived query

> **"What new $20 / $50 / $100 physical-agent products became possible this month because component costs crossed a threshold?"**

## Hierarchy

> **POW = physical capability/data infrastructure**
> **tiny consumer brands = experiments/spinouts built from POW discoveries**
