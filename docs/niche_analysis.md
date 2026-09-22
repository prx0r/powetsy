# Competitive Landscape & Niche Analysis

**Date:** 22 September 2026

## Current Strategy (5 sentences)

POWEtsy aims to normalize the fragmented Chinese physical-AI supply chain into a programmable API for agents. It targets consumer physical-agent products (desk companions, plant agents, pet robots) that share commodity hardware. The near-term product is a Build Recipe system starting from known-good modules. It explicitly avoids manufacturing — stopping at validated recipe + quote + supplier routing. The moat is the accumulated manufacturing outcome graph (actual MOQ, prices, lead times, defect rates).

## Competitor Landscape

### AI PCB Design (well-funded, ~$70M+ combined)

| Company | Does | Doesn't Do |
|---------|------|-----------|
| **Flux.ai** | AI PCB design + live sourcing + MCP | No mechanical, no enclosure, no manufacturing routing |
| **CELUS** | NL → schematic + BOM | No PCB routing, no mechanical, no manufacturing |
| **Quilter** | Autonomous PCB layout | No design, no mechanical, no manufacturing |
| **JITX** | Design-as-code for PCBs | No manufacturing, no cross-domain |

### Manufacturing Marketplaces

| Company | Does | Doesn't Do |
|---------|------|-----------|
| **Madeinair** | AI quotes from 50K+ factories | No product intelligence, no recipe system |
| **OpenFactory** | MCP API for factory search + quoting | No design intelligence, only 10+ factories |
| **Factorem** | CNC/molding quotes | Mechanical only, no electronics |
| **ZeroMOQ** | No-MOQ manufacturing | No design intelligence |
| **Tianxia Gongchang** | 4.8M Chinese factories + API | No BOM knowledge, no recipe system |

### Component Databases (saturated)

| Company | Does | Doesn't Do |
|---------|------|-----------|
| **Octopart/Nexar** | Component search + pricing | No design intelligence |
| **SiliconExpert** | 1B+ parts, lifecycle, compliance | No design automation |
| **BOMwise** | AI BOM cost optimization | No manufacturing routing |
| **PartGenie** | 22M parts, alternatives | No recipe system |

### Physical Agent Platforms

| Company | Does | Doesn't Do |
|---------|------|-----------|
| **Fdata** | Robot ODM with open APIs | Traditional ODM, no AI design |
| **Wellwit** | Modular robot platforms | Traditional ODM |
| **Videostrong** | Companion robot ODM | No programmable layer |
| **autonomous-os** | OS for physical AI agents | No hardware recipes, no supply chain |

## The Gap

**Nobody combines:**
- Cross-domain product composition (PCB + enclosure + actuators + firmware + assembly)
- Physical agent domain knowledge (which modules work together)
- Module-first design (avoid custom PCB until demand validates)
- Manufacturing outcome graph (actual vs claimed MOQ, prices, lead times)

## Our Niche

> **Product intelligence layer BEFORE the EDA tools and BEFORE the manufacturing marketplaces.**

Flux/Quilter answer: "How do I route this trace?"
Makerfabs answers: "Which factory can make this?"
**POW answers: "What should I build, from what, and where?"**

## Risk Assessment

| Risk | Level | Mitigation |
|------|-------|-----------|
| Flux/CELUS expands into full product composition | High | They're PCB-level. Cross-domain is harder. Move fast on recipe graph. |
| Tianxia Gongchang adds product intelligence | High | They have factories but not "which components work together." |
| Market too early | Medium | Data garden produces other outputs while waiting. |
| Chinese sourcing complexity | Medium | This IS why the abstraction layer is valuable. |
| Makerfabs/Seeed build their own platform | Low | They're factories, not platforms. They benefit from intermediation. |

## Bottom Line

**Yes, there is a real gap.** The $70M+ EDA space handles PCB design. The manufacturing marketplace space handles factory routing. Nobody handles the cross-domain product intelligence layer that connects "what should I build" to "how do I actually build it" for physical agent products.

The defense is speed and domain depth: build the recipe graph, outcome data, and substitution intelligence first, and make it API-first so it becomes the default query layer before anyone touches an EDA tool or contacts a factory.
