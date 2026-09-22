# Assembly Reality — The Missing Physical Step

## The Clean Model

All parts converge on one assembly partner. They build/test/package, then ship.

## Build Recipe = Design + BOM + Fabrication + Assembly

```
DESIGN:      CAD / geometry
BOM:         what to buy
FABRICATION: what needs printing/PCB/CNC
ASSEMBLY:    how all pieces become one object
TEST:        validation
```

## Supplier Assembly Capabilities (Verified)

| Supplier | PCB | Mech | Final Assembly | Test | Fulfilment |
|----------|-----|------|----------------|------|------------|
| PCBWay | ✓ | ✓ | ✓ box build | ✓ | delivery |
| Makerfabs | ✓ | ✓ | ✓ | ✓ | ✓ dropship |
| Seeed Fusion | ✓ | ✓/ODM | ✓ | ✓ | ✓ warehouse+fulfill |
| Fdata | ✓/SMT | ✓ | ✓ | ✓ | delivery |
| Haidewei | electronics | ✓ housing | ✓ | ✓ | ✓ |

## The Build Package

```
design/    enclosure.step, gerbers/, bom.csv, pick_place.csv
assembly/  instructions.json, wiring.json, exploded_view.png
software/  firmware.bin, flash_instructions.json
test/      functional_test.json, acceptance_criteria.json
commercial/ quantity, target_cost, destination, packaging
```

## Volume Progression

```
qty=1:    off-the-shelf modules + manual assembly
qty=10:   modules + batch fabrication + jigs
qty=100:  custom carrier PCB + assembly house
qty=1000: integrated PCB + optimized Chinese components
```

## The V0 Path

Kit: printed shell + compute board + servos + cables + screws + firmware.
Customer: plug, snap, screw.
```

