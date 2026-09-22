# Critique — Failure Modes & Corrections

## 1. "Physical compiler" sounds cleaner than reality

Generated CAD can be geometrically valid while still being a terrible product.

Manufacturing involves tolerance stacks, thermal behavior, EMI/EMC, cable routing, serviceability, vibration, fastener access, assembly sequence, calibration, safety, certification and test fixtures.

**Weaken early promise to:**

> POW converts constrained, known classes of physical designs into validated build recipes.

## 2. Supplier abstraction is not enough moat

Makerfabs already does PCB design, PCBA, sourcing, mechanical design, 3D printing, molding, final assembly, testing, certification, packaging and drop shipping.

**POW needs to be better at the step *before* the EMS company:**

> What architecture should this product use, given cost, quantity, compatibility, existing successful designs, failures and available substitutes?

## 3. One-unit manufacturing is misleading economically

```text
parts                 $22
printing               9
assembly/test         18
China domestic         4
international shipping 15
payment/handling       4
support/returns        8
─────────────────────────
effective cost        $80
```

First abstraction should be:

```
KNOWN CORE + KNOWN PERIPHERALS + GENERATED SHELL + GENERATED SOFTWARE
```

## 4. Infinity of product ideas is dangerous

Choose narrow initial family:

```
DESKTOP / HOME PHYSICAL AGENTS
camera, mic, speaker, display, RGB, servo, ESP32/Linux SBC, USB-C, battery, sensors, 3D print
```

## 5. Ontology trap

Don't spend six months inventing schemas. Start from actual machines.

Pick 10-20 devices, fully decompose, find shared components.

## 6. Chinese sourcing is harder than it sounds

Modules don't have durable MPNs, stable docs or consistent revisions.

Need identity model accepting uncertainty:

```
manufacturer-known exact part
manufacturer-family
supplier SKU
listing/revision
observed physical variant
probable-equivalent
```

## 7. Substitutes need dimensions

```text
functional, electrical, mechanical, pin, software, thermal, regulatory, observed-in-practice
```

Distinguish: inferred compatibility vs observed successful substitution.

## 8. "AI agents are the customer" is premature

Better immediate customer: **hardware builder wants cheaper/replacement architecture.**

> "Here is my current BOM. Reduce cost 25% without changing external behavior."

## 9. Manufacturing routing can become ugly

Early POW should stop at:

```
validated recipe + quote + supplier routing + export package
```

Not merchant-of-record.

## 10. Certification may kill cute ideas

Graph should model: regulatory_complexity, certification_required, shipping_constraints, battery constraints, radio constraints.

## 11. Not all data is moat-worthy

Valuable: machine decompositions, actual BOMs, observed substitutions, failure histories, historical cost, manufacturing quote history, assembly paths, real supplier outcomes.

Not valuable: "we have our own copy of LCSC."

## 12. Competitive risk from design platforms

Flux already integrates real-time supply-chain data.

Defense: **cross-domain physical composition** — PCB + motor + gearbox + housing + camera + fasteners + firmware + repair evidence + actual deployments.

## 13. May be early enough that demand doesn't monetize yet

Data garden can have other outputs: component research, repair intelligence, BOM indexes, investment signals, new-product discovery, internal experiments.

## What to actually do

Build the world's best graph of **20 inexpensive physical-agent machines**:

```
5 desktop robots
5 cheap mobile robots
5 smart-home/agent devices
5 open-source robotics builds
```

For each, manually achieve 90%+ subsystem understanding.

Find shared components. Create three reference benchmarks.

Test one hard query: **Given a device, can POW propose a cheaper version using evidence-backed substitutions?**

If yes, the larger thesis becomes credible.
