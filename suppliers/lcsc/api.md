# LCSC Electronics — API Details

## API
- Base URL: https://ips.lcsc.com
- Auth: API key + HMAC signature (nonce + timestamp + signature)
- Apply: https://fat.lcsc.com/agent
- Docs: https://www.lcsc.com/docs/openapi/index.html

## Endpoints
- GET /rest/wmsc2agent/category — all categories
- GET /rest/wmsc2agent/manufacturer — all manufacturers
- GET /rest/wmsc2agent/search — keyword/MPN/category search
- GET /rest/wmsc2agent/product/{lcsc_part_number} — item details
- POST /rest/wmsc2agent/order — create order
- POST /rest/wmsc2agent/cart — manage cart

## Limits
- Default: 1,000 searches/day, 200/minute
- Higher limits by approval

## Data Available
- MPN, manufacturer, category, description
- Stock quantities (real-time)
- Tiered pricing (CNY/USD/EUR/HKD)
- Datasheet URLs
- Compliance (ECCN/HTS)
- Package/pin info
- Lifecycle status
- EasyEDA symbol/footprint references

## Coverage
- 760,000+ in-stock SKUs
- 4,400+ manufacturers
- Category/manufacturer enumeration
- Product change notifications feed

## Python Client
- https://github.com/suiang/PyLCSC (community)
- https://github.com/eggfly/easyeda-agent-skills (EasyEDA integration)
