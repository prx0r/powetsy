# Physical Design Compiler

> **Design anything. Give POW the files and constraints. Get back a buildable recipe, quote and reorderable physical product.**

## The Product

```text
INPUT
──────────────
CAD / STEP / STL / KiCad / BOM
or simply requirements

quantity: 1
target price: $60
ship to: UK
priority: cheapest
```

POW then does:

```text
1. UNDERSTAND      geometry, electronics, interfaces, functional requirements
2. RESOLVE         off-the-shelf Chinese components, motors, cameras, sensors
3. FABRICATION     buy commodity / PCB/PCBA / FDM/SLS/SLA / CNC / sheet metal
4. COMPATIBILITY   voltages, connectors, dimensions, protocols, drivers, mounts
5. ROUTING         supplier A → motors, B → electronics, C → chassis, D → assembly
6. QUOTE           1 / 10 / 100 / 1,000 units
7. BUILD           prototype
8. SAVE            immutable Build Recipe
9. REORDER         one click
```

## The Build Recipe

```text
MONSTERA BOT v1.3

Last ordered: 12 units
Current unit price: $34.18
Previous: $37.42
Parts changed: camera module A → A2
Reason: A discontinued
Compatibility: verified

[ ORDER 1 ] [ ORDER 10 ] [ ORDER 100 ]
```

## The Compiler

```text
pow compile robot.step \
  --target-cost 40 \
  --quantity 10 \
  --optimize cheapest

→
BUILDABLE: yes
ESTIMATED UNIT COST: $36.14
ASSEMBLY: $7.22
SHIPPING: $3.80
LEAD TIME: 11–17 days

17 commodity parts, 3 printed parts, 1 assembled PCB
4 substitutions made, 2 geometry changes suggested, 1 supply-chain risk
```

Optimization flags: --cheapest, --fastest, --UK-parts, --china, --repairable, --lowest-moq, --highest-reliability, --open-hardware, --mass-production

## The Flywheel

Every build teaches POW. 428,000 attempted builds reveals:

- Most designs requiring 2-axis motion under $30 converge on 3 servo families
- This camera is frequently selected but rejected for poor Linux driver
- 38% of designs become viable if actuator falls below $12
- SLS cheaper than FDM around quantity 24
- Chinese motor dominates substitute market for 3 Western products

## Two Gardens

```text
EXTERNAL GARDEN: watch physical reality
INTERNAL GARDEN: watch what people are trying to instantiate
```

The second may eventually be more valuable.

## Supplier Abstraction

```text
supplier_182: PCB_ASSEMBLY, SMT, THT, PROGRAMMING, FUNCTIONAL_TEST
supplier_392: SLS_PA12, SLA_RESIN
supplier_551: CNC_6061, CNC_7075
supplier_827: FINAL_ASSEMBLY, PACKAGING, FULFILMENT
```

Customer sees: Monstera Bot v1.3. Not which factories in Bao'an.

## The Endgame

> **POW = manufacturing compiler for generated physical designs.**
