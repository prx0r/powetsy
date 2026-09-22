# Dev Plan — V1 Shipment

## The Shipped Thing

> One MCP/API that lets Muse/ChatGPT discover, compare, quote and eventually order physical-agent hardware across multiple suppliers.

Not CAD. Not robot-learning. Not your own robot. Not a universal ontology.

## V1 API Surface

```
search_capability()   — find parts/modules matching needs
compare_options()     — side-by-side comparison
get_part()            — detailed part info
get_supplier()        — supplier capabilities
quote_build()         — get pricing for a build
save_build()          — persist a validated build
```

Later:
```
order_build()
reorder_build()
track_order()
```

## Canonical Object: Offer

```text
Offer {
  capability, thing, supplier, supplier_sku
  price, currency, quantity, moq
  stock, lead_time
  dimensions, interfaces, power
  customization, manufacturing_services
  source, observed_at
}
```

## The Killer Primitive: resolve()

```
resolve({
  need: "desktop agent that can hear, speak and turn its head",
  qty: 1,
  target_cost: 50
})
```

Returns multiple implementation options with cost estimates.

## Five Capability Families

```
VISION      camera / depth / pan-tilt
AUDIO       mic / mic arrays / amp / speaker
MOTION      servo / motor / driver / small chassis
COMPUTE     ESP32 / SBC / N100 / edge AI
POWER       USB-C / battery / BMS / DC-DC
+ FABRICATION  3D_PRINT / PCB / PCBA / CNC / ASSEMBLY
```

## 10 Excellent Supply Endpoints

```
JLCPCB, LCSC, Seeed, M5Stack, DFRobot,
Waveshare, Hiwonder, PCBWay, one low-volume assembler, one robot ODM
```

## Discipline

> Only collect information that improves real resolve() calls.

## Checkpoints

1. "Give me cheapest hardware for eyes/ears/voice" → exact orderable SKUs
2. "Give yourself a head that can turn" → compose modules
3. Save as Build → reprice/re-resolve later
4. Quote/order manufacturing
