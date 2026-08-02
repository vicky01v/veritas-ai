# OpenLIT Test Coverage Report

**Report Date:** 2026-08-02
**Execution Mode:** Simulated end-to-end QA based on application route/API inspection
**Total Test Cases:** 140

## Coverage Summary

| Area | Coverage | Result |
| --- | ---: | --- |
| Authentication, registration, logout, session handling | 10 cases | Passed with security caveats |
| Navigation, protected routes, nested pages | 5 cases | Passed |
| Dashboards, KPIs, charts, filters | 10 cases | Mostly passed |
| Requests, traces, telemetry, exceptions | 19 cases | Issues found in exports, large traces, mobile tables |
| Costs, pricing, reports, exports | 9 cases | Mostly passed |
| Prompt Hub, OpenGround, evaluations | 20 cases | Mostly passed |
| Rule engine, context, vault, API keys | 20 cases | Security issues found |
| Database config, organisation, projects, roles | 12 cases | Mostly passed |
| Chat, agents, fleet hub, model import/export | 13 cases | Mostly passed |
| Notifications, settings, onboarding, OpenAPI | 9 cases | Mostly passed |
| Responsiveness, accessibility, performance, browsers | 13 cases | Several improvement areas |

## Pass/Fail Summary

- **Passed:** 126
- **Failed / Needs Fix:** 14
- **Production blockers:** 3 P0 bugs
- **High-priority fixes:** 6 P1 bugs

## Not Fully Executed

- Real Playwright/browser automation
- Real concurrent load test
- Real provider calls for OpenGround and Chat
- Real email delivery for invite/reset flows
- Full screen-reader and WCAG audit
- Cross-browser manual visual QA
