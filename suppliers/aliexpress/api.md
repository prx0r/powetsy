# AliExpress — API Details

## API
- Open Platform: https://developer.alibaba.com
- Product API available (with auth)
- Price, stock, SKU-level data
- Localized sale prices, delivery-day filtering

## Role in POW
Cheapest packaged module versions. Discovery source for "what can I order one of cheaply right now?"

## Caveat
Listings, not canonical engineering parts. Same product from 8 sellers, silent revisions.

Normalize as:
```
LISTING → seller, SKU, price, shipping, reviews
```
not:
```
CANONICAL_PART
```

Link listings to canonical parts where evidence allows.
