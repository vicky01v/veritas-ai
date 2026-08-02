# OpenLIT Risk Assessment

**Report Date:** 2026-08-02
**Production Readiness Score:** 78/100
**Recommendation:** Demo-ready with seeded data; production release should wait for P0/P1 fixes.

## Critical Risks

| Risk | Severity | Impact | Mitigation |
| --- | --- | --- | --- |
| Vault or API key exposure | Critical | Customer secrets could leak through UI, logs, or network traces | Enforce redaction, one-time reveal, server-only secret handling, and security tests |
| Stale dashboard data after rapid navigation | Critical | Users may make decisions from incorrect KPIs | Abort in-flight widget requests and ignore stale responses |
| Trace detail memory growth | Critical | Long sessions can crash browser tabs | Virtualize large span trees and clean chart/listener resources |

## High Risks

| Risk | Severity | Impact | Mitigation |
| --- | --- | --- | --- |
| Query timeout under concurrent dashboard usage | High | Dashboards may show partial data or errors | Cache common aggregations and optimize ClickHouse queries |
| Timezone inconsistency | High | Charts/reports may disagree across regions | Centralize timezone formatting |
| Project/database config scoping regression | High | Users may see wrong project config or lose access | Add project-scoped API and selector tests |
| Provider misconfiguration during demo | High | OpenGround/Chat can fail in front of clients | Preflight provider setup or use mocked responses |

## Medium Risks

| Risk | Severity | Impact | Mitigation |
| --- | --- | --- | --- |
| Mobile table overflow | Medium | Poor mobile experience for operational views | Responsive card rows or column chooser |
| Weak export feedback | Medium | Users may trigger duplicate jobs or think export failed | Async export status and notifications |
| Incomplete accessibility coverage | Medium | Keyboard/screen-reader gaps may remain | Full WCAG audit and icon-label pass |

## Final Recommendation

Use the current app for a controlled 10-15 minute live demo after seeding data. Do not position it as fully production-ready until critical security, data integrity, and memory issues are fixed and verified with automated tests.
