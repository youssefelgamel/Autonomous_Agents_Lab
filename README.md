# Swiftrail Logistics Company

## About Us

We are a logistics company specializing in managing large-scale shipments through railway transportation combined with road delivery. Our goal is to ensure fast, reliable, and cost-effective shipment delivery while minimizing delays.

---

# ⚠️ The Problem

Shipment delays caused by:

- Traffic congestion
- Vehicle breakdowns
- Bad weather
- Customer unavailability

These delays may lead to missed schedules, customer dissatisfaction, and increased operational costs.

---

# 🤖 Why AI Agents?

Traditional logistics systems only monitor shipment status.

AI Agents can:

- Detect problems automatically.
- Decide the best action.
- Use external tools.
- Reduce delivery delays.
- Improve customer satisfaction.

---

# Agent Architectures

This project implements the four agent architectures introduced in the Agent Design Lab.

## 1. Reactive Agent

A rule-based agent.

- No LLM.
- Uses predefined if/else rules.
- Every delay type maps directly to a fixed action.

Example:

```
Traffic
    ↓
Change Route
```

---

## 2. Unconstrained ReAct Agent

A free-form reasoning agent powered by an LLM.

Features:

- Uses ReAct (Thought → Action → Observation).
- Chooses its own reasoning.
- Decides which tool to call.
- Can perform multiple reasoning steps.
- Stops only when it decides the problem is solved.

Example:

```
Thought
    ↓
check_traffic()
    ↓
Observation
    ↓
Thought
    ↓
change_route()
    ↓
Observation
    ↓
notify_customer()
    ↓
Final Answer
```

---

## 3. Deterministic Routing Agent

Uses a single LLM call.

The model only classifies the shipment into one category.

Example:

```
Shipment Report
        ↓
LLM Classification
        ↓
MINOR_DELAY
        ↓
handle_minor_delay()
```

The routing logic is completely deterministic after classification.

---

## 4. Constrained ReAct Agent

A structured ReAct agent.

Features:

- Uses ReAct reasoning.
- Restricted to approved tools only.
- Structured JSON output using Pydantic.
- Tool validation.
- Maximum reasoning loop.
- Explicit Finish action.

Example:

```
Thought
    ↓
get_train_status()
    ↓
Observation
    ↓
Thought
    ↓
get_weather()
    ↓
Observation
    ↓
Thought
    ↓
reroute_shipment()
    ↓
Observation
    ↓
Finish
```

---

# Technologies

- Python
- Gemini API
- OpenRouter
- Pydantic
- dotenv

---

# Project Structure

```
Autonomous_Agents_Lab
│
├── Reactive
├── Unconstrained_React
├── Routing
└── Constrained_React
```

---

# Comparison Between Agent Architectures

| Feature | Reactive | Unconstrained ReAct | Deterministic Routing | Constrained ReAct |
|----------|----------|---------------------|-----------------------|-------------------|
| Uses LLM | ❌ | ✅ | ✅ (One Call) | ✅ |
| Reasoning | ❌ | ✅ Free-form | ❌ | ✅ Structured |
| Tool Selection | Fixed Rules | Model Chooses | Fixed Handler | Restricted Tools |
| Multiple Steps | ❌ | ✅ | ❌ | ✅ |
| Output Format | Rule Result | Natural Language | Category | Structured JSON |
| Predictability | High | Low | High | High |
| Flexibility | Low | Very High | Medium | High |
| Safety | High | Low | High | Very High |

---

# Summary

| Agent | Strength | Weakness |
|--------|----------|----------|
| Reactive | Fast and simple | No reasoning |
| Unconstrained ReAct | Most flexible and intelligent | Can make unpredictable decisions |
| Deterministic Routing | Fast and consistent | Limited flexibility after classification |
| Constrained ReAct | Balances reasoning with safety | Slightly more complex implementation |

---
