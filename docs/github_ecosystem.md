# GitHub Ecosystem Review — POWEtsy Landscape

## Three Layers Map to Our Stack

| Layer | Key Projects | What It Does |
|-------|-------------|--------------|
| Design/BOM | hardware-foundry, Hermod, BuildSheet-Phoenix, BOM_Analyzer | NL → manufacturable specs |
| Agent Runtime | PhyAgentOS, autonomous-os, esp-claw, rai | AI brain on physical hardware |
| Manufacturing | mcp-mes, forge-mcp, eryxon-flow | Route production through factories |

## The Gap

Nobody connects all three into a single "configure → manufacture → deploy" workflow for consumer physical AI agents. That's POWEtsy's opportunity.

## Most Directly Relevant

| Project | Stars | Why It Matters |
|---------|-------|---------------|
| **Hermod-Robotics/Hermod** | ~100 | One hardware YAML → firmware + URDF + ROS2 + BOM. THE product configurator. |
| **PhyAgentOS** | 1,666 | Most popular physical AI OS. Decouples brain from body. |
| **autonomous-ai/autonomous-os** | 20 | "Android for physical agents." HAL maps to our configurator. |
| **broml/Project_Emily** | ~100 | Full ESP32 companion from off-the-shelf parts. |
| **YuGu0358/hardware-foundry** | ~1 | NL → BOM + PCB + STL + firmware + assembly docs. |
| **maddiedreese/vibe-coding-for-hardware** | ~50 | Manifesto for non-engineers building hardware with AI. |
| **slopus/codex-keybored** | ~10 | End-to-end: Fusion360 → KiCad → STM32 → JLC quotes. |
| **autonomous-ai/autonomous-vibe** | 23 | "Describe → print it" with Bambu Lab integration. |

## Key Insight

The biggest projects (PhyAgentOS 1.6K stars, Hermod 100 stars) prove the agent runtime layer is converging. But none of them handle manufacturing routing. POWEtsy sits at the intersection:
- Above: agent runtimes (PhyAgentOS, autonomous-os)
- Below: manufacturing (mcp-mes, forge-mcp)
- Connecting: design → reality
