"""20 canonical machines — narrowed scope per critique.

5 desktop robots, 5 smart-home/agent devices, 5 cheap mobile robots,
5 open-source robotics builds.
"""

MACHINES_20 = {
    # === DESKTOP ROBOTS (5) ===
    'sesame-robot': {
        'name': 'Sesame ESP32 Quadruped',
        'type': 'quadruped_robot', 'category': 'desktop_robot',
        'description': '8-servo quadruped, $50-60, 3D printed',
        'subsystems': {
            'actuation': ['servo:sg90_x8'],
            'compute': ['mcu:esp32'],
            'power': ['battery:2s_lipo'],
        },
    },
    'reachy-mini': {
        'name': 'Reachy Mini',
        'type': 'desktop_robot', 'category': 'desktop_robot',
        'description': 'Open-source AI robot, camera, 4-mic, speaker, 9 servos',
        'subsystems': {
            'compute': ['soc:raspberry_pi_cm4'],
            'sensing': ['camera:usb_wide', 'mic:4array', 'imu:icm42688'],
            'actuation': ['servo:dynamixel_xl330_x9'],
            'audio': ['speaker:small', 'amp:class_d'],
            'power': ['psu:5v_usb_c'],
        },
    },
    'm5stack-atom-voice': {
        'name': 'M5Stack ATOM Voice',
        'type': 'ai_endpoint', 'category': 'desktop_robot',
        'description': 'Programmable smart-speaker module, $13.50',
        'subsystems': {
            'compute': ['mcu:esp32'],
            'sensing': ['mic:mems'],
            'audio': ['speaker:small'],
            'comms': ['wifi:esp32', 'bluetooth:ble'],
        },
    },
    'q8bot': {
        'name': 'Q8Bot Miniature Quadruped',
        'type': 'quadruped_robot', 'category': 'desktop_robot',
        'description': 'PCB-spine quadruped, no wires, $300-400',
        'subsystems': {
            'actuation': ['servo:dynamixel_xl330_x8'],
            'compute': ['mcu:esp32'],
            'power': ['battery:3s_lipo', 'buck:5v'],
        },
    },
    'mochi-robot': {
        'name': 'MOchi OLED Robot',
        'type': 'expressive_head', 'category': 'desktop_robot',
        'description': 'Minimalist OLED expression robot, touch-responsive',
        'subsystems': {
            'compute': ['mcu:esp32'],
            'sensing': ['capacitive_touch'],
            'display': ['oled:096'],
            'power': ['usb_c'],
        },
    },

    # === SMART HOME / AGENT DEVICES (5) ===
    'plant-agent': {
        'name': 'Plant Agent Basic',
        'type': 'plant_monitor', 'category': 'agent_device',
        'description': 'ESP32 plant monitor, moisture/light/temp + RGB',
        'subsystems': {
            'compute': ['mcu:esp32s3'],
            'sensing': ['soil_moisture', 'bh1750', 'sht30'],
            'output': ['ws2812b_led'],
            'power': ['usb_c'],
        },
    },
    'desk-agent': {
        'name': 'Desk Agent Button',
        'type': 'control_surface', 'category': 'agent_device',
        'description': 'Physical button/knob/LED for personal AI agent',
        'subsystems': {
            'compute': ['mcu:esp32s3'],
            'sensing': ['rotary_encoder', 'tactile_button_x2'],
            'display': ['oled:096'],
            'output': ['ws2812b_led'],
            'power': ['usb_c'],
        },
    },
    'mood-lamp': {
        'name': 'Ambient Mood Lamp',
        'type': 'smart_light', 'category': 'agent_device',
        'description': 'AI-controlled color lamp with presence sensing',
        'subsystems': {
            'compute': ['mcu:esp32s3'],
            'sensing': ['pir_sensor', 'sht30'],
            'output': ['ws2812b_led_x2'],
            'power': ['usb_c'],
        },
    },
    'voice-puck': {
        'name': 'AI Voice Puck',
        'type': 'voice_assistant', 'category': 'agent_device',
        'description': 'Compact ESP32 voice assistant',
        'subsystems': {
            'compute': ['mcu:esp32s3'],
            'sensing': ['inmp441_mic'],
            'audio': ['max98357a_amp', 'speaker:3w'],
            'output': ['ws2812b_led'],
            'power': ['usb_c'],
        },
    },
    'env-station': {
        'name': 'Room Environment Station',
        'type': 'sensor_station', 'category': 'agent_device',
        'description': 'Multi-sensor room monitoring with display',
        'subsystems': {
            'compute': ['mcu:esp32s3'],
            'sensing': ['sht30', 'bh1750', 'mq135'],
            'display': ['oled:096'],
            'power': ['usb_c'],
        },
    },

    # === CHEAP MOBILE ROBOTS (5) ===
    'hiwonder-miniauto': {
        'name': 'Hiwonder miniAuto Pro',
        'type': 'omnidirectional_rover', 'category': 'mobile_robot',
        'description': 'ESP32 omnidirectional AI robot, ~$90',
        'subsystems': {
            'actuation': ['motor:mecanum_x4'],
            'compute': ['mcu:esp32_p4'],
            'sensing': ['camera:ov2640', 'imu:mpu6050'],
            'power': ['battery:7.4v_lipo'],
        },
    },
    'linorobot2': {
        'name': 'Linorobot2 AMR',
        'type': 'ackerman_rover', 'category': 'mobile_robot',
        'description': 'ROS2 autonomous mobile robot',
        'subsystems': {
            'actuation': ['motor:dc_geared_x2', 'driver:l298n'],
            'compute': ['soc:raspberry_pi_4', 'mcu:esp32'],
            'sensing': ['lidar:ydlidar_x4', 'camera:usb', 'imu:mpu6050'],
            'power': ['battery:12v_7ah', 'buck:5v'],
        },
    },
    'esp32-drone': {
        'name': 'ESP32 Mini Drone',
        'type': 'quadcopter', 'category': 'mobile_robot',
        'description': 'WiFi-controlled mini drone, Crazyflie-based',
        'subsystems': {
            'actuation': ['motor:brushless_x4', 'esc:1s_x4'],
            'compute': ['mcu:esp32'],
            'sensing': ['imu:mpu6050', 'barometer'],
            'power': ['battery:1s_lipo'],
            'comms': ['wifi:esp32'],
        },
    },
    'crazyflie-clone': {
        'name': 'Crazyflie-compatible FC',
        'type': 'flight_controller', 'category': 'mobile_robot',
        'description': 'Open-source ESP32 flight controller',
        'subsystems': {
            'compute': ['mcu:esp32'],
            'sensing': ['imu:bmi088', 'barometer:bmp388'],
            'actuation': ['motor:brushless_x4', 'esc:1s_x4'],
            'power': ['battery:1s_lipo'],
        },
    },
    'rover-ackerman': {
        'name': 'Ackerman Steering Rover',
        'type': 'ackerman_rover', 'category': 'mobile_robot',
        'description': '4-wheel Ackerman with servo steering',
        'subsystems': {
            'actuation': ['motor:dc_geared_x2', 'servo:sg90'],
            'compute': ['mcu:esp32'],
            'sensing': ['imu:mpu6050', 'ultrasonic:hc_sr04'],
            'power': ['battery:6v_aa_x4'],
        },
    },

    # === OPEN-SOURCE ROBOTICS BUILDS (5) ===
    'opencat-esp32': {
        'name': 'OpenCat ESP32 Quadruped',
        'type': 'quadruped_robot', 'category': 'open_hardware',
        'description': '8-servo quadruped, ESP32-S3, Petoi ecosystem',
        'subsystems': {
            'actuation': ['servo:petoi_x8'],
            'compute': ['mcu:esp32s3'],
            'power': ['battery:2s_lipo'],
        },
    },
    'mjbots-quad': {
        'name': 'mjbots quad A1',
        'type': 'quadruped_robot', 'category': 'open_hardware',
        'description': 'Open-source quadruped, qdd100 actuators',
        'subsystems': {
            'actuation': ['actuator:qdd100_x4'],
            'compute': ['soc:raspberry_pi_4', 'mcu:stm32'],
            'power': ['battery:6s_lipo'],
            'comms': ['can:transceiver'],
        },
    },
    'robotont-driver': {
        'name': 'Robotont Motor Driver',
        'type': 'motor_driver_pcb', 'category': 'open_hardware',
        'description': 'KiCad motor driver, JLCPCB-ready',
        'subsystems': {
            'power_stage': ['mosfet:irfz44n_x4', 'driver:l298n'],
            'control': ['mcu:stm32'],
            'interface': ['connector:xt60', 'connector:jst'],
        },
    },
    '4can-hat': {
        'name': '4CAN Raspberry Pi HAT',
        'type': 'interface_board', 'category': 'open_hardware',
        'description': '4x CAN bus HAT for Raspberry Pi',
        'subsystems': {
            'interface': ['can:transceiver_x4', 'can:socketcan'],
            'compute': ['soc:raspberry_pi'],
            'connector': ['gpio:40pin'],
        },
    },
    'open-simple-lidar': {
        'name': 'Open Simple LiDAR',
        'type': 'lidar_module', 'category': 'open_hardware',
        'description': 'DIY scanning laser rangefinder',
        'subsystems': {
            'sensing': ['laser:940nm', 'detector:apd'],
            'compute': ['mcu:stm32'],
            'mechanical': ['motor:stepper', 'bearing:optical'],
        },
    },
}
