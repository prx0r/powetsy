# Nexar / Octopart — API Details

## API
- GraphQL: https://api.nexar.com/graphql
- Docs: https://support.nexar.com/
- Free tier available (limited)

## Capabilities
- Cross-distributor price/stock/availability
- MPN resolution
- Quantity price breaks from multiple sellers
- Lifecycle status
- Datasheet links
- Alternative/cross-reference parts

## Key Query
```graphql
query {
  supSearchMpn(q: "STM32G431", limit: 10) {
    hits {
      mpn
      manufacturer { name }
      sellers {
        company { name }
        offers {
          inventoryLevel
          moq
          mpq
          unitPrice
          currency
          url
        }
      }
    }
  }
}
```

## Value
Cross-distributor normalization. One query gets prices from DigiKey, Mouser, Farnell, Arrow, LCSC etc.
