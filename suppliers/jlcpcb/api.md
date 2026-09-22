# JLCPCB — API Details

## APIs

### Components API
- Search millions of parts
- Specifications, live inventory, pricing
- Parts compatible with JLC assembly

### PCB API
- Upload Gerbers → auto-quote → order → track
- Endpoint: POST /api/overseas/openapi/pcb/wip/get
- Upload: POST /api/overseas/openapi/pcb/upload
- Create: POST /api/overseas/openapi/pcb/create

### 3D Printing API
- Upload STL/STEP → auto-quote → order → track
- Processes: SLA, MJF, SLM, FDM, SLS

### Auth
- HMAC signature: METHOD\nURI\nTIMESTAMP\nNONCE\nBODY
- Apply: https://api.jlcpcb.com

## Notes
- Component inventory is for JLC assembly workflow
- Standalone component pickup has restrictions/fees
- LCSC is cleaner for raw parts purchasing
- JLC is the manufacturing endpoint
