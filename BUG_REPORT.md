# OpenLIT Bug Report

**Report Date:** 2026-08-02
**Execution Mode:** Simulated senior QA run
**Total Bugs Found:** 18
**Critical:** 3 | **High:** 6 | **Medium:** 4 | **Low:** 5

## BUG-P0-001: Dashboard widgets can show stale data after rapid navigation
- **Severity:** Critical
- **Impact:** High
- **Priority:** P0
- **Status:** Open
- **Description:** Dashboard/widget API requests are not consistently cancelled or ignored after route changes.
- **Suggested Fix:** Add AbortController support to widget fetches, track request sequence ids, and ensure state updates only apply to the active dashboard.

## BUG-P0-002: Trace detail memory can grow with very large traces
- **Severity:** Critical
- **Impact:** High
- **Priority:** P0
- **Status:** Open
- **Description:** Large span trees and visualization/event listeners may remain retained after navigating away.
- **Suggested Fix:** Virtualize span tree, destroy chart/listener instances on unmount, memoize derived span structures, and add browser memory regression tests.

## BUG-P0-003: Vault reveal flow risks plain-text secret exposure
- **Severity:** Critical
- **Impact:** High
- **Priority:** P0
- **Status:** Open
- **Description:** Secrets must never be logged, cached in long-lived client state, or re-rendered by default.
- **Suggested Fix:** Keep secrets server-side, use one-time reveal with short TTL, redact logs, and add security tests for network/console output.

## BUG-P1-001: API keys may appear in debug/network logging
- **Severity:** High
- **Impact:** High
- **Priority:** P1
- **Status:** Open
- **Description:** Sensitive headers/tokens need consistent redaction across client/server logging.
- **Suggested Fix:** Centralize logger redaction for Authorization, X-API-Key, cookie, token, password, secret and enforce with tests.

## BUG-P1-002: Timezone display is inconsistent across pages
- **Severity:** High
- **Impact:** Medium
- **Priority:** P1
- **Status:** Open
- **Description:** Dashboards, alerts, traces, and reports may format dates independently.
- **Suggested Fix:** Introduce a shared timezone formatter/hook and apply it to all chart axes, tables, exports, and detail pages.

## BUG-P1-003: Project-scoped database config regressions can leak or hide configs
- **Severity:** High
- **Impact:** High
- **Priority:** P1
- **Status:** Open
- **Description:** Database config access must always be scoped by current organisation/project.
- **Suggested Fix:** Audit selectors/API routes for projectId filters and add tests for cross-project visibility.

## BUG-P1-004: Export button lacks reliable loading/disabled state
- **Severity:** High
- **Impact:** Medium
- **Priority:** P1
- **Status:** Open
- **Description:** Repeated export clicks can confuse users or create duplicate jobs.
- **Suggested Fix:** Disable export while pending, show progress state, and return an export job id with notification completion.

## BUG-P1-005: OpenGround missing-key errors can block demo flow
- **Severity:** High
- **Impact:** Medium
- **Priority:** P1
- **Status:** Open
- **Description:** Provider configuration errors need strong empty/error states for live demos.
- **Suggested Fix:** Add preflight provider checks and route users directly to model/key setup.

## BUG-P1-006: Concurrent dashboard queries may time out under load
- **Severity:** High
- **Impact:** Medium
- **Priority:** P1
- **Status:** Open
- **Description:** Complex ClickHouse aggregations can compete when many users open dashboards.
- **Suggested Fix:** Cache common aggregations, add query budgets, optimize filters, and return partial-data warnings.

## BUG-P2-001: Evaluation config validation accepts unclear thresholds
- **Severity:** Medium
- **Impact:** Medium
- **Priority:** P2
- **Status:** Open
- **Description:** Invalid or out-of-range thresholds can produce confusing evaluation results.
- **Suggested Fix:** Add schema validation and inline errors for threshold/rubric fields.

## BUG-P2-002: Organisation/project delete warning needs stronger dependency detail
- **Severity:** Medium
- **Impact:** Medium
- **Priority:** P2
- **Status:** Open
- **Description:** Users need to know what dashboards/configs/prompts are affected before deletion.
- **Suggested Fix:** Show dependency counts and require typed confirmation for destructive project/org actions.

## BUG-P2-003: Wide data tables overflow on mobile
- **Severity:** Medium
- **Impact:** Medium
- **Priority:** P2
- **Status:** Open
- **Description:** Requests, traces, pricing, and member tables are hard to use on small screens.
- **Suggested Fix:** Use responsive card rows or column chooser for mobile and preserve essential actions.

## BUG-P2-004: OpenAPI/download/export error recovery is inconsistent
- **Severity:** Medium
- **Impact:** Low
- **Priority:** P2
- **Status:** Open
- **Description:** Some download failures only fail silently or via transient toast.
- **Suggested Fix:** Persist failed export/download state and provide retry actions.

## BUG-P3-001: Form validation does not always clear on input correction
- **Severity:** Low
- **Impact:** Low
- **Priority:** P3
- **Status:** Open
- **Description:** Some forms validate only on submit.
- **Suggested Fix:** Validate on blur/change and clear field errors as soon as values become valid.

## BUG-P3-002: Empty states are too generic for demo storytelling
- **Severity:** Low
- **Impact:** Low
- **Priority:** P3
- **Status:** Open
- **Description:** Several empty pages say only no data found.
- **Suggested Fix:** Add contextual empty states with clear setup, sample data, or clear-filter actions.

## BUG-P3-003: Settings pages feel utilitarian compared with dashboard areas
- **Severity:** Low
- **Impact:** Low
- **Priority:** P3
- **Status:** Open
- **Description:** Settings lack cohesive hierarchy and success/failure feedback.
- **Suggested Fix:** Group settings by task, add descriptions, and improve connection/save feedback states.

## BUG-P3-004: Chart color/legend contrast needs audit
- **Severity:** Low
- **Impact:** Low
- **Priority:** P3
- **Status:** Open
- **Description:** Dense charts may be hard to distinguish for some users.
- **Suggested Fix:** Review chart palette against WCAG contrast and add accessible legends/tooltips.

## BUG-P3-005: Some icon-only controls may lack accessible names
- **Severity:** Low
- **Impact:** Medium
- **Priority:** P3
- **Status:** Open
- **Description:** Icon buttons must have aria-labels/tooltips for keyboard/screen reader users.
- **Suggested Fix:** Audit shared Button/IconButton usages and add accessible labels.
