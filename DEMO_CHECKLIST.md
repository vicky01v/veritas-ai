# OpenLIT Live Demo Checklist

## Environment

- [ ] App starts successfully from `src/client`.
- [ ] Default seeded login works: `user@openlit.io` / `openlituser`.
- [ ] ClickHouse is running if telemetry dashboards are shown.
- [ ] Prisma seed has created default organisation, project, user, and DB config.
- [ ] `scripts/generate-demo-data.py` has populated telemetry when ClickHouse is available.
- [ ] `demo_business_data.json` exists for mock/report/dashboard fixtures.

## Demo Data

- [ ] Dashboard has non-empty KPIs and charts.
- [ ] Requests table has success and error traces.
- [ ] Trace detail has prompt, response, model, token, latency, and cost data.
- [ ] Evaluations include passing and failing examples.
- [ ] Prompt Hub has at least 3 polished prompts.
- [ ] OpenGround has provider configuration or mocked responses.
- [ ] Vault and API key examples are masked.
- [ ] Notifications include unread, read, export, and alert examples.
- [ ] Reports/exports have at least one ready file.

## Demo Flow

- [ ] Login.
- [ ] Browse dashboard and filter date/service/model.
- [ ] Search and sort Requests.
- [ ] Open a trace detail.
- [ ] Review costs and export a report.
- [ ] Create/edit/delete a prompt or rule.
- [ ] Compare models in OpenGround.
- [ ] Show evaluations and rule engine.
- [ ] Rotate/revoke a masked API key or secret.
- [ ] Mark notifications as read.
- [ ] Logout.

## Avoid During Demo

- [ ] Do not open very large traces repeatedly until memory cleanup is fixed.
- [ ] Do not reveal real secrets or provider keys.
- [ ] Do not rely on live external model providers unless keys and quotas are confirmed.
- [ ] Do not use mobile viewport for data-table-heavy walkthroughs.
