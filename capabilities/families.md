# Capability Families

## VISION

```yaml
vision:
  camera:
    - usb_camera_basic: "Generic USB camera, 720p-1080p, rolling shutter, $8-15"
    - usb_camera_global: "Arducam B0322, OV2311, 2MP global shutter, USB, $25-30"
    - rpi_camera_3: "Raspberry Pi Camera Module 3 Wide, IMX708, 12MP, CSI, $35"
    - dfrobot_ov9281: "DFRobot OV9281, 1MP global shutter, MIPI-CSI, $25.90"
    - esp32_cam: "ESP32-CAM module, OV2640, WiFi, $5-8"
  depth:
    - realsense_d455: "Intel RealSense D455, stereo depth, USB3, ~$300"
    - oak_d_luxonis: "Luxonis OAK-D, stereo depth + AI, USB3, ~$150"
    - tof_vl53l1x: "VL53L1X ToF sensor, 4m range, I2C, $5-10"
  pan_tilt:
    - sg90_2axis: "2× SG90 servos + 3D printed bracket, $5-8"
    - ds3218_2axis: "2× DS3218 servos + bracket, $20-30"
    - dynamixel_2axis: "2× XL330 + bracket, $40-60"
```

## AUDIO

```yaml
audio:
  microphone:
    - inmp441: "INMP441 I2S MEMS mic, $2-3"
    - sph0645: "SPH0645 I2S MEMS mic, $3-5"
    - respeaker_2mic: "Seeed reSpeaker 2-Mic HAT, $15"
    - respeaker_4mic: "Seeed reSpeaker XVF3800, 4-mic array, $55"
  amplifier:
    - max98357a: "MAX98357A I2S Class D amp, 3W, $2-3"
    - pam8403: "PAM8403 Class D amp, 2×3W, $1-2"
    - tp3116: "TP3116 Class D amp, 2×50W, $5-8"
  speaker:
    - speaker_3w: "3W 4Ω speaker, $1-3"
    - speaker_5w: "5W 4Ω speaker, $3-5"
    - speaker_8ohm: "8Ω full-range, $5-10"
```

## MOTION

```yaml
motion:
  servo:
    - sg90: "SG90 9g micro servo, 1.8kg·cm, $1-2"
    - ds3218: "DS3218 20kg metal gear, $8-12"
    - sts3215: "Feetech STS3215, 19kg·cm, serial bus, $13.89"
    - xl330: "Dynamixel XL330, $20-30"
    - xl430: "Dynamixel XL430, ~$50"
  motor_driver:
    - simplefoc_mini: "SimpleFOC Mini, BLDC FOC, $13"
    - simplefoc_shield: "SimpleFOC Shield v3.2, $25"
    - odrive_micro: "ODrive Micro, BLDC FOC, $89"
    - waveshare_st3215: "Waveshare ST3215 board, serial bus, $10.60"
    - tb6612fng: "TB6612FNG dual H-bridge, $3-5"
    - bts7960: "BTS7960 dual H-bridge, 43A, $3-8"
  encoder:
    - as5600: "AS5600 magnetic absolute, 12-bit, I2C, $2-5"
    - as5048a: "AS5048A magnetic absolute, 14-bit, SPI, $15"
    - amt102v: "CUI AMT102-V incremental, $27.50"
```

## COMPUTE

```yaml
compute:
  esp32:
    - esp32s3: "ESP32-S3, dual-core 240MHz, WiFi+BLE, AI accelerator, $3-5"
    - esp32c3: "ESP32-C3, RISC-V 160MHz, WiFi+BLE, $2-3"
    - esp32: "ESP32, dual-core 240MHz, WiFi+BLE, $2-4"
  sbc:
    - rpi5: "Raspberry Pi 5, BCM2712, 8GB, $80"
    - rpi_zero2w: "Raspberry Pi Zero 2W, $15"
    - jetson_orin_nano: "Jetson Orin Nano, 40 TOPS, $249"
    - jetson_orin_nx: "Jetson Orin NX, 100 TOPS, $399"
  mini_pc:
    - n100: "Intel N100 mini PC, 16GB, 500GB NVMe, $120-180"
    - n100_fanless: "Fanless N100, 16GB, 256GB, $100-140"
```

## POWER

```yaml
power:
  usb:
    - usb_c_5v: "USB-C 5V power supply, $3-8"
    - usb_c_pd: "USB-C PD trigger board, $2-5"
  battery:
    - lipo_2s: "2S LiPo 7.4V 1000mAh, $8-12"
    - lipo_3s: "3S LiPo 11.1V 1000mAh, $12-18"
    - lifepo4_12v: "12V LiFePO4 2000mAh, $20-30"
  dc_dc:
    - buck_5v: "LM2596 buck converter, 4.5-40V→5V 3A, $1-2"
    - buck_3v3: "AMS1117-3.3V LDO, $0.50"
    - buck_12v: "XL4015 buck, 8-36V→12V 5A, $2-4"
  bms:
    - bms_2s: "2S LiPo BMS, $1-2"
    - bms_3s: "3S LiPo BMS, $2-3"
```

## FABRICATION

```yaml
fabrication:
  pcb:
    - jlcpcb_basic: "JLCPCB 2-layer, from $2 for 5pcs"
    - jlcpcb_4layer: "JLCPCB 4-layer, from $5 for 5pcs"
  pcba:
    - jlcpcb_smt: "JLCPCB SMT assembly, $8.18 setup + $0.0016/joint"
  print_3d:
    - jlcpcb_sla: "JLCPCB SLA resin, from $5"
    - jlcpcb_fdm: "JLCPCB FDM, from $5"
    - pcbway_sls: "PCBWay SLS PA12, from $10"
    - pcbway_cnc: "PCBWay CNC, from $25"
  enclosure:
    - fdm_printed: "FDM printed enclosure, $2-10"
    - sla_printed: "SLA printed enclosure, $5-20"
    - sls_printed: "SLS printed enclosure, $10-40"
```
