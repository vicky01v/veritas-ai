# OpenLIT Live Demo Script and Checklist

**Duration:** 10-15 minutes
**Audience:** Customer executives, engineering leads, AI platform owners, product managers
**Demo Account:** `user@openlit.io` / `openlituser`

## Presenter Flow

### 1. Login and Positioning (1 minute)
Log in as the demo user and explain that OpenLIT gives teams one place to observe, evaluate, debug, and optimize AI applications. Point out the current organisation/project selector so the audience understands multi-project scoping.

### 2. Dashboard Overview (2 minutes)
Open `/playground/dashboard`. Walk through request volume, cost, tokens, latency, error rate, and quality KPIs. Change the time range to Last 24 Hours, then filter to a production service. Explain that executives get cost and adoption visibility while engineers get operational health.

### 3. Requests to Trace Drilldown (2 minutes)
Open Requests, search for `gpt-4o`, sort by latency, filter errors, and open a trace. Show the span tree, prompt, model, token counts, cost, response, and error/evaluation metadata. Explain how this shortens incident debugging.

### 4. Costs and Reports (1 minute)
Open Costs/Pricing. Filter by provider/model, show custom pricing, then trigger/export a cost report. Mention the completion notification and generated report download.

### 5. Prompt Hub and OpenGround (2 minutes)
Open Prompt Hub, create or edit a demo prompt, compile variables, then open OpenGround and compare two model responses. Explain prompt versioning, model comparison, latency, quality, and cost tradeoffs.

### 6. Evaluations and Rule Engine (2 minutes)
Open Evaluations and show pass/fail trends for toxicity, hallucination, relevance, and safety. Create or show an evaluation type. Open Rule Engine and demonstrate routing a condition like provider/model/application to a prompt/context/evaluator.

### 7. Vault, API Keys, and Settings (1 minute)
Open Vault and API key settings. Create a masked secret/API key, rotate/revoke it, and stress that secret values should remain masked. Show database config test connection and org/project settings.

### 8. Agents, Fleet, and Notifications (1 minute)
Open Agents/Fleet Hub and show operational status. Open notifications, mark all as read, and explain how completed exports, failures, and quality issues surface to users.

### 9. End Flow (30 seconds)
Search/filter one more record, export/import model config if time allows, then log out. Summarize: OpenLIT connects telemetry, debugging, cost, quality, prompt management, and operations into one workflow.

## Demo Checklist

- [ ] App starts locally and login works.
- [ ] Default account exists from Prisma seed.
- [ ] ClickHouse is running when telemetry dashboards are shown.
- [ ] `scripts/generate-demo-data.py` has populated telemetry data.
- [ ] `demo_business_data.json` exists for mock/report/dashboard fixtures.
- [ ] At least one provider key or mock response path is configured for OpenGround/Chat.
- [ ] Prompt Hub contains 3-5 polished prompts.
- [ ] Evaluations contain passing and failing examples.
- [ ] Requests table has successful and failed traces.
- [ ] Exports/downloads are pretested.
- [ ] Notifications have unread and read examples.
- [ ] Browser zoom is 100%; viewport is desktop width.
- [ ] P0/P1 risks are not triggered during the demo path.

## Client-Facing Talk Track for CRUD Simulation

- **Create:** “I’ll add a new prompt and save it as a reusable, versioned asset for the team.”
- **Edit:** “Now I’ll change the prompt wording and keep the previous version available for rollback.”
- **Delete:** “For cleanup, I’ll delete or archive a test rule after confirming the dependency warning.”
- **Search:** “I can search by model, trace ID, service, or prompt name to find a specific record quickly.”
- **Filter:** “Every operational view supports narrowing by time, service, provider, environment, model, and status.”
- **Export:** “This report export preserves the active filters so teams can share the exact slice they investigated.”
- **Import:** “Model config import lets teams move provider/model settings between environments.”
- **Notifications:** “Completed exports and operational alerts arrive as notifications, so users do not need to wait on long jobs.”
- **Logout:** “The session ends cleanly and protected routes redirect back to login.”
