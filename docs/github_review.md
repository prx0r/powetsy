# POWEtsy — GitHub Project Review

**Date:** 22 September 2026

## Executive Summary

Found 40+ open-source projects across 12 categories relevant to physical AI agents. The ecosystem is surprisingly mature — especially for ESP32-based devices. The strongest signal is that **the same hardware patterns repeat across categories**: ESP32 + mic + speaker + LEDs + servos + sensors. This validates the three-node architecture (SENSE/EXPRESS/MOTION).

## Highest-Value Projects

### Tier 1: Directly Useful (production-ready patterns)

| Project | Stars | Why It Matters |
|---------|-------|---------------|
| **wled/WLED** | 18,600 | De facto LED controller. 200+ effects, audio-reactive, HA integration. Our lighting kit should be WLED-compatible. |
| **esphome/esphome** | 11,600 | De facto smart home node framework. 200+ components. Our sensor/control kits should have ESPHome recipes. |
| **dorianborian/sesame-robot** | 4,242 | Best open-source small robot. $50-60 BOM, 8 servos, OLED face. Proves our price point works. |
| **espressif/esp-drone** | 2,100 | Official mini drone. WiFi control, iOS/Android app. Proves drone kit is viable. |
| **LedFx/LedFx** | 2,000 | Audio-reactive LED effects engine. Pairs with WLED. |
| **atomic14/esp32_audio** | 463 | I2S audio reference: INMP441 mic, MAX98357A amp. Our audio kit should use these exact parts. |
| **srg74/WLED-wemos-shield** | 558 | WLED shield PCB. Shows exactly how to make a WLED-compatible hardware product. |

### Tier 2: Reference Implementations

| Project | Stars | Why It Matters |
|---------|-------|---------------|
| **ovidiu4/smart-plant-monitor** | 196 | Plant monitor: ESP32-S3, solar, e-paper, 45x45mm. Our plant kit should learn from this. |
| **cifertech/ESP32-Drone** | ~200 | ESP32 drone flight stack. Shows what's possible with commodity parts. |
| **playfultechnology/esp32-eyes** | ~200 | Emotive OLED eyes. Our expressive head kit should integrate this. |
| **espressif/esp-va-sdk** | 316 | Official voice assistant SDK. Alexa/Google integration path. |
| **sheaivey/ESP32-AudioInI2S** | 80 | MEMS mic + FFT + visualization. Audio kit reference. |

### Tier 3: Component References

| Project | Stars | Why It Matters |
|---------|-------|---------------|
| **PierceBrandies/PetFeeder** | 30 | Pet camera + YOLOv8. Shows pet kit architecture. |
| **whiteSHADOW1234/PetCam** | 21 | Pet camera + two-way audio. Simpler architecture. |
| **MatsRobot/Face-Tracking** | ~5 | Pan/tilt face tracking. Camera kit reference. |
| **cerevisis/ESP32-Weather-Station** | 9 | Weather station. Sensor kit reference. |

## Key Patterns Observed

### The ESP32 Core Stack

Nearly every project uses some combination of:

```
ESP32-S3 or ESP32-C3
+ INMP441 or SPH0645 mic
+ MAX98357A or PAM8403 amp
+ WS2812B or SK6812 LEDs
+ SG90 or DS3218 servos
+ OLED 0.96" or 1.3" display
+ SHT30/BME280 temp/humidity
+ BH1750 light sensor
+ USB-C power
```

This validates the three-node architecture perfectly.

### Recurring Component Choices

| Component | Projects Using | Our Reference |
|-----------|---------------|---------------|
| ESP32-S3 | 20+ | ✅ Agent Node |
| INMP441 mic | 8+ | ✅ Hear Kit |
| MAX98357A amp | 6+ | ✅ Audio Kit |
| WS2812B LEDs | 15+ | ✅ Light Kit |
| SG90 servo | 10+ | ✅ Motion Kit |
| OLED 0.96" | 8+ | ✅ Desk Kit |
| SHT30 | 5+ | ✅ Sense Kit |
| BH1750 | 4+ | ✅ Sense Kit |

### BOM Price Validation

| Product Type | Our Target | GitHub Reality |
|-------------|-----------|---------------|
| Plant monitor | $25 | $15-30 (solar adds cost) |
| Desk agent | $35 | $25-40 |
| Pet camera | $45 | $30-50 |
| Mood lamp | $30 | $15-25 |
| Voice puck | $20 | $15-25 |
| Desktop head | $40 | $30-50 |
| Pan/tilt camera | $30 | $25-40 |
| Mini drone | $50-100 | $40-80 |

## What POW Should Do With These

### 1. Create Edge Recipes

For each top project, create a `powetsy` recipe:

```yaml
recipe: sesame-robot
source: github:dorianborian/sesame-robot
bom:
  - esp32s3
  - sg90_servo x8
  - oled_096
  - 3d_printed_frame
total_cost: ~$55
difficulty: intermediate
personalization: [character, colors, gaits, animations]
```

### 2. Track Component Adoption

Every project that uses ESP32-S3 + INMP441 + MAX98357A is evidence that this combination works. Count projects using each component → adoption score.

### 3. Detect Recurring Patterns

If 15 projects all use ESP32-S3 + mic + speaker + LED, that's a **physical agent primitive** worth integrating into a kit.

### 4. Price History

For components used in >5 projects, start tracking price/stock on LCSC. That's where POW's history moat begins.

## Recommended Immediate Actions

1. **Create recipes** for the top 10 projects in powetsy seeds
2. **Wire adoption scores** — count GitHub projects using each component
3. **Start LCSC price tracking** for the 8 most-used components
4. **Build WLED/ESPHome compatibility** into the lighting/sensor kits
5. **Study sesame-robot BOM** — it's the best reference for our maker category
