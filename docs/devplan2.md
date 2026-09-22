# Dev Plan 2 — Supplier Integration + MCP Server

## Three Supplier Classes

1. **API-native** — LCSC, JLCPCB, Waveshare, Nexar, Arrow, Farnell, TME
2. **Structured catalog** — DFRobot, M5Stack, Seeed, AliExpress
3. **Marketplace/factory discovery** — 1688, Alibaba ODM, direct Shenzhen

## Integration Sequence

### Week 1 (Tier S)
LCSC, JLCPCB, Waveshare, Nexar

### Week 2 (Tier A)
DFRobot, M5Stack, Seeed, AliExpress

### Week 3 (Tier A global)
Arrow, Farnell, TME

### Week 4+ (Tier B)
1688, Alibaba ODM, direct Shenzhen

## V1 Test
Ask for 10 capabilities at 1/10/100 units. Get back cheapest + best-supported + global alternative + China price + Western price + stock + MOQ + shipping + exact source.

## MCP API
search_capability, compare_options, get_part, get_supplier, quote_build, save_build, resolve
