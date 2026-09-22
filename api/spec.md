# MCP API Specification

## V1 Endpoints

### search_capability

Find parts/modules matching functional requirements.

```python
search_capability(
    capability: str,           # "vision", "audio", "motion", etc.
    requirements: dict,        # {"camera": true, "usb": true, "linux": true}
    max_price: float = None,   # Maximum unit price
    currency: str = "USD",
    region: str = None         # "UK", "CN", "global"
) -> list[Offer]
```

### compare_options

Side-by-side comparison of candidate solutions.

```python
compare_options(
    options: list[str],        # Part/offer IDs to compare
    criteria: list[str]        # ["price", "availability", "compatibility"]
) -> ComparisonTable
```

### get_part

Detailed information about a specific part.

```python
get_part(
    part_id: str
) -> PartDetail
```

### get_supplier

Supplier capabilities and current status.

```python
get_supplier(
    supplier_id: str
) -> SupplierInfo
```

### quote_build

Get pricing for a complete build at various quantities.

```python
quote_build(
    build_id: str,
    quantities: list[int] = [1, 10, 100, 1000]
) -> Quote
```

### save_build

Persist a validated build for later reordering.

```python
save_build(
    name: str,
    parts: list[BuildItem],
    metadata: dict = None
) -> BuildId
```

### resolve (the killer primitive)

High-level capability resolution.

```python
resolve(
    need: str,                 # Natural language description
    qty: int = 1,
    target_cost: float = None,
    constraints: dict = None    # {"region": "UK", "repairable": true}
) -> list[BuildOption]
```

## Response Types

### Offer
```python
@dataclass
class Offer:
    capability: str
    thing: str              # Part name/description
    supplier: str           # Supplier ID
    supplier_sku: str
    price: float
    currency: str
    quantity: int
    moq: int
    stock: int
    lead_time_days: int
    dimensions: dict
    interfaces: list[str]
    power: str
    source: str
    observed_at: str
```

### BuildOption
```python
@dataclass
class BuildOption:
    name: str
    description: str
    parts: list[BuildItem]
    estimated_cost: float
    currency: str
    manufacturing_route: str
    confidence: float
    evidence: list[str]
```

### BuildItem
```python
@dataclass
class BuildItem:
    capability: str
    part_id: str
    part_name: str
    supplier: str
    supplier_sku: str
    quantity: int
    role: str
    notes: str
```
