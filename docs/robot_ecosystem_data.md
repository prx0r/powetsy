# Robot Ecosystem Data Collection

**Date:** 22 September 2026

## LeRobot Compatible Robots

| Robot | Manufacturer | DOF | Cost | Servos | LeRobot Driver |
|-------|-------------|-----|------|--------|---------------|
| SO-101 | TheRobotStudio | 6 | ~$122 | 6× STS3215 | FeetechMotorsBus |
| SO-100 | TheRobotStudio | 6 | ~$115 | 6× STS3215 | FeetechMotorsBus |
| Koch v1.1 | Tau Robotics | 6 | ~$250 | XL330/XL430 | DynamixelMotorsBus |
| OpenArm | Community | 7 | ~$450 | Damiao (CAN FD) | DamiaoMotorsBus |
| OMX | RobotShop | 5 | ~$299 | Dynamixel | DynamixelMotorsBus |
| LeKiwi | SIGRobotics | 6+3w | ~$184 | 3× STS3215 | FeetechMotorsBus |
| Reachy Mini | Pollen | 9 | $399-499 | XL330/XC330 | Pollen SDK |
| Unitree G1 | Unitree | 29 | ~$16K | Unitree | Unitree SDK |

## SO-101 BOM (Follower Arm)

| Component | Qty | Price | Source |
|-----------|-----|-------|--------|
| STS3215 7.4V 1/345 (C001) | 7 | $13.89 ea | Alibaba |
| STS3215 7.4V 1/191 (C044) | 2 | $13.89 ea | Alibaba |
| STS3215 7.4V 1/147 (C046) | 3 | $13.89 ea | Alibaba |
| Waveshare Motor Control Board | 2 | $10.60 ea | Amazon |
| USB-C Cable | 1 | $7.00 | Amazon |
| 5V 5A PSU | 2 | $10.00 ea | Amazon |
| Table Clamps | 1 | $9.00 | Amazon |
| Screwdriver Set | 1 | $6.00 | Amazon |
| **Total** | | **~$230** | |

## Cheapest Arms Under $500

| Arm | Single | Pair | DOF |
|-----|--------|------|-----|
| SO-101 | $122 | $230 | 6 |
| SO-100 | $115 | $225 | 6 |
| LeKiwi | $184 | — | 6+3w |
| Koch v1.1 | $250 | $477 | 6 |
| OMX | — | $299 | 5 |

## Chinese Servo Suppliers

| Supplier | Key Product | Price | Protocol |
|----------|-----------|-------|----------|
| Feetech | STS3215 | $13.89 | TTL serial bus |
| Feetech | STS3250 | $40-47 | TTL serial bus |
| Hiwonder | LX-224 | $15.99 | TTL serial |
| Dynamixel | XL330 | $20-30 | TTL/RS-485 |
| Dynamixel | XM430 | ~$100 | TTL/RS-485 |
| Damiao | Various | $50+ | CAN FD |

## ESP32 Robot Controllers

| Board | Price | Features |
|-------|-------|----------|
| Cytron Robo ESP32 | $16.40 | 2× DC, 4× servo |
| DFRobot Romeo ESP32-S3 | $46.90 | 4ch H-bridge, camera |
| ESP32-DOIT-DevKit | $8-12 | External drivers |
| NullLab Maker-ESP32-Pro | $20-25 | 4 DC + 4 servo + encoder |

## Camera Modules Under $30

| Camera | Sensor | Shutter | Interface | Price |
|--------|--------|---------|-----------|-------|
| Arducam B0322 | OV2311 | Global | USB | $25-30 |
| DFRobot OV9281 | OV9281 | Global | MIPI-CSI | $25.90 |
| Generic USB | Various | Rolling | USB | $8-15 |

## Motor Drivers

| Driver | Type | Price |
|--------|------|-------|
| SimpleFOC Mini | BLDC FOC | $13 |
| SimpleFOC Shield v3.2 | BLDC FOC | $25 |
| ODrive Micro | BLDC FOC | $89 |
| ODrive S1 | BLDC FOC | $162 |
| Waveshare ST3215 Board | Serial bus | $10.60 |
| TB6612FNG | DC brushed | $3-5 |
| BTS7960 | DC brushed | $3-8 |

## Encoders

| Encoder | Type | Price |
|---------|------|-------|
| AS5600 | Magnetic absolute | $2-5 |
| AS5048A | Magnetic absolute | $15 |
| CUI AMT102-V | Incremental | $27.50 |
| Feetech STS3215 | Built-in 12-bit | Included |
| Dynamixel XL330 | Built-in 12-bit | Included |

## Open-Source BOMs Under $500

| Project | Cost | Key Parts |
|---------|------|-----------|
| SO-101 pair | $230 | 12× STS3215, Waveshare boards |
| SO-101 single | $122 | 6× STS3215 |
| LeKiwi wired | $184 | 3× STS3215, omni wheels |
| Sesame Quadruped | $50-60 | 8× MG90, ESP32 |
| 3we Platform | $95 | ESP32-S3, N20 motors |
