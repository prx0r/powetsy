# Robot Infrastructure Moat

## Positioning

Not "become a robot-learning researcher." Instead:

> **The grounded supply / compatibility / manufacturing graph that every robotics stack needs.**

As software gets standardized (LeRobot, ACT, SmolVLA), the scarce layer becomes:

```
Which physical platform?
Which actuator?
Which camera?
Which motor controller?
Which supplier?
What does it cost?
What replaces it?
What actually works?
What breaks?
Who can manufacture it?
```

## Learn at operator/infrastructure depth, not researcher depth

Understand enough LeRobot to know what customers mean by:
- robot configuration, joint/action space, observations
- camera streams, teleoperation, calibration
- dataset recording, policy deployment, hardware plugin

Understand enough hardware to know:
- servo bus, encoder, gear reduction, motor torque
- camera interface, power requirements
- CAN/UART/USB, mounting geometry

Do NOT spend months on policy gradients.

## One essential exercise

Build/obtain one cheap LeRobot-compatible arm (SO-101). Take it through:

```
buy parts → assemble → flash → calibrate → teleoperate
→ record dataset → train ACT/SmolVLA → deploy → break
→ source replacement
```

Turn it into data collection, not a portfolio project.

## Four priority datasets

1. **Platform decomposition** — robot → subsystem → part → supplier → interface → substitute
2. **Supplier graph** — MOQ, pricing, customization, lead time, actual outcomes
3. **Compatibility graph** — LeRobot/ROS2/Linux/SDK support per device
4. **Substitution + outcomes** — what replaces what, what actually works

## The killer query

```
pow.resolve_robot({
    observations: ["rgb", "joint_position"],
    actions: ["6dof_arm"],
    framework: "lerobot",
    budget: 400,
    region: "UK"
})
```

Returns actual machines/components/suppliers.

## The moat

> Whatever intelligence you use, POW tells it how to instantiate itself physically.

INTELLIGENCE ↓ cost → therefore scarce: physical actuators, sensors, power, fabrication, supply chains, compatibility, deployment knowledge.
