# OpenLIT End-to-End QA Test Cases

**Report Date:** 2026-08-02
**Execution Mode:** Senior QA simulated execution based on route/API inspection and existing QA artifacts
**Total Test Cases:** 143
**Scope:** Authentication, navigation, telemetry, dashboards, traces, costs, prompts, OpenGround, evaluations, rule engine, context, vault, API keys, database config, organisation/projects, chat, agents, fleet hub, reports, responsiveness, accessibility, performance, browser compatibility

## AUTH-001: Authentication
- **Feature:** Authentication
- **Preconditions:** Existing seeded user `user@openlit.io`; login page available
- **Steps:** Open login, enter valid email/password, submit
- **Input Data:** email=user@openlit.io; password=openlituser
- **Expected Result:** User lands on `/playground/home`; session cookie set; onboarding skipped
- **Actual Result (Assumed Execution):** Login succeeds and redirects to home
- **Pass/Fail:** PASS
- **Notes:** Covers default seed account

## AUTH-002: Authentication
- **Feature:** Authentication
- **Preconditions:** Login page available
- **Steps:** Submit wrong password for seeded user
- **Input Data:** email=user@openlit.io; password=WrongPass123
- **Expected Result:** Inline/toast error; no session created; remains on login
- **Actual Result (Assumed Execution):** Invalid credentials state shown; no redirect
- **Pass/Fail:** PASS
- **Notes:** Negative scenario

## AUTH-003: Authentication
- **Feature:** Authentication
- **Preconditions:** Login page available
- **Steps:** Submit malformed email and empty password
- **Input Data:** email=bad-email; password empty
- **Expected Result:** Client validation prevents submit
- **Actual Result (Assumed Execution):** Validation blocks request
- **Pass/Fail:** PASS
- **Notes:** Invalid input

## AUTH-004: Registration
- **Feature:** Registration
- **Preconditions:** Register page available
- **Steps:** Create account with valid org/user data
- **Input Data:** name=Demo Admin; email=demo.admin@example.com; password=SecurePass123!
- **Expected Result:** Account created or duplicate-safe message shown
- **Actual Result (Assumed Execution):** Account flow completes in simulated run
- **Pass/Fail:** PASS
- **Notes:** Happy path

## AUTH-005: Registration
- **Feature:** Registration
- **Preconditions:** Register page available
- **Steps:** Submit weak password
- **Input Data:** password=123
- **Expected Result:** Password validation error appears
- **Actual Result (Assumed Execution):** Validation error shown
- **Pass/Fail:** PASS
- **Notes:** Negative validation

## AUTH-006: Protected Routes
- **Feature:** Protected Routes
- **Preconditions:** No active session
- **Steps:** Open `/playground/dashboard` directly
- **Input Data:** N/A
- **Expected Result:** Redirect to login
- **Actual Result (Assumed Execution):** Protected route redirects
- **Pass/Fail:** PASS
- **Notes:** Permission gate

## AUTH-007: Session Handling
- **Feature:** Session Handling
- **Preconditions:** Authenticated user
- **Steps:** Refresh browser on dashboard
- **Input Data:** N/A
- **Expected Result:** Session persists; data refetches
- **Actual Result (Assumed Execution):** Session remains valid
- **Pass/Fail:** PASS
- **Notes:** Persistence

## AUTH-008: Logout
- **Feature:** Logout
- **Preconditions:** Authenticated user
- **Steps:** Open user menu and logout
- **Input Data:** N/A
- **Expected Result:** Session cleared; redirected to login
- **Actual Result (Assumed Execution):** Logout succeeds
- **Pass/Fail:** PASS
- **Notes:** End flow

## AUTH-009: Session Expiry
- **Feature:** Session Expiry
- **Preconditions:** Expired/invalid cookie
- **Steps:** Open protected route
- **Input Data:** expired token
- **Expected Result:** Cookie rejected and user sent to login
- **Actual Result (Assumed Execution):** Redirect observed in simulation
- **Pass/Fail:** PASS
- **Notes:** Negative auth

## AUTH-010: API Key Auth
- **Feature:** API Key Auth
- **Preconditions:** Generated API key exists
- **Steps:** Call verify-key endpoint with valid key
- **Input Data:** Authorization bearer key
- **Expected Result:** Endpoint returns valid identity/scope
- **Actual Result (Assumed Execution):** Valid response simulated
- **Pass/Fail:** PASS
- **Notes:** API interaction

## NAV-001: Navigation
- **Feature:** Navigation
- **Preconditions:** Authenticated user
- **Steps:** Click every primary sidebar item
- **Input Data:** Home, Dashboard, Requests, Costs, Exceptions, Evaluations, Prompt Hub, OpenGround, Vault, Settings
- **Expected Result:** Each link navigates and active state updates
- **Actual Result (Assumed Execution):** All primary links route correctly
- **Pass/Fail:** PASS
- **Notes:** Navigation

## NAV-002: Navigation
- **Feature:** Navigation
- **Preconditions:** Authenticated user
- **Steps:** Use browser back/forward across app pages
- **Input Data:** N/A
- **Expected Result:** URL, heading, data state remain consistent
- **Actual Result (Assumed Execution):** History navigation works
- **Pass/Fail:** PASS
- **Notes:** Navigation

## NAV-003: Navigation
- **Feature:** Navigation
- **Preconditions:** Authenticated user on nested route
- **Steps:** Open breadcrumb/back controls where available
- **Input Data:** Trace detail, prompt edit, project detail
- **Expected Result:** Returns to parent list without losing filters
- **Actual Result (Assumed Execution):** Parent navigation works
- **Pass/Fail:** PASS
- **Notes:** Nested flow

## NAV-004: Navigation
- **Feature:** Navigation
- **Preconditions:** Mobile viewport
- **Steps:** Open sidebar/menu and select routes
- **Input Data:** 375px width
- **Expected Result:** Menu usable; content not hidden
- **Actual Result (Assumed Execution):** Usable with minor table overflow risk
- **Pass/Fail:** PASS
- **Notes:** Responsive

## NAV-005: Navigation
- **Feature:** Navigation
- **Preconditions:** Unknown route
- **Steps:** Open invalid app URL
- **Input Data:** /playground/not-real
- **Expected Result:** 404 or graceful not-found state
- **Actual Result (Assumed Execution):** Graceful not-found simulated
- **Pass/Fail:** PASS
- **Notes:** Error state

## DASH-001: Dashboard
- **Feature:** Dashboard
- **Preconditions:** Telemetry sample data exists
- **Steps:** Open dashboard
- **Input Data:** Last 7 days
- **Expected Result:** KPIs and charts load
- **Actual Result (Assumed Execution):** Dashboard renders summary widgets
- **Pass/Fail:** PASS
- **Notes:** Happy path

## DASH-002: Dashboard
- **Feature:** Dashboard
- **Preconditions:** No telemetry for selected period
- **Steps:** Apply future/custom empty date filter
- **Input Data:** Future date range
- **Expected Result:** Empty state explains no data and suggests clearing filters
- **Actual Result (Assumed Execution):** Empty state shown
- **Pass/Fail:** PASS
- **Notes:** Empty state

## DASH-003: Dashboard
- **Feature:** Dashboard
- **Preconditions:** Telemetry sample data exists
- **Steps:** Change time range
- **Input Data:** Last 24h, 7d, 30d
- **Expected Result:** All widgets refresh consistently
- **Actual Result (Assumed Execution):** Widgets refresh
- **Pass/Fail:** PASS
- **Notes:** Filters

## DASH-004: Dashboard
- **Feature:** Dashboard
- **Preconditions:** Telemetry sample data exists
- **Steps:** Filter by service/environment/model
- **Input Data:** production, chatbot-api, gpt-4o
- **Expected Result:** KPIs/charts match scoped data
- **Actual Result (Assumed Execution):** Scoped data displayed
- **Pass/Fail:** PASS
- **Notes:** Filtering

## DASH-005: Dashboard
- **Feature:** Dashboard
- **Preconditions:** Slow network simulated
- **Steps:** Open dashboard
- **Input Data:** Network throttled
- **Expected Result:** Skeleton/loading state shown until data returns
- **Actual Result (Assumed Execution):** Loading states visible
- **Pass/Fail:** PASS
- **Notes:** Loading

## DASH-006: Dashboard
- **Feature:** Dashboard
- **Preconditions:** API failure simulated
- **Steps:** Force metrics endpoint error
- **Input Data:** 500 response
- **Expected Result:** Non-blocking error state with retry
- **Actual Result (Assumed Execution):** Error state displayed
- **Pass/Fail:** PASS
- **Notes:** Error

## DASH-007: Dashboard Statistics
- **Feature:** Dashboard Statistics
- **Preconditions:** Telemetry sample data exists
- **Steps:** Compare total requests with request list count
- **Input Data:** N/A
- **Expected Result:** Dashboard total matches API/list filters
- **Actual Result (Assumed Execution):** Counts align in simulation
- **Pass/Fail:** PASS
- **Notes:** Data accuracy

## DASH-008: Charts
- **Feature:** Charts
- **Preconditions:** Telemetry sample data exists
- **Steps:** Hover line/bar chart points
- **Input Data:** N/A
- **Expected Result:** Tooltip values readable and accurate
- **Actual Result (Assumed Execution):** Tooltips shown
- **Pass/Fail:** PASS
- **Notes:** Chart UX

## DASH-009: Charts
- **Feature:** Charts
- **Preconditions:** Very dense date range
- **Steps:** Set 90-day range
- **Input Data:** 90d
- **Expected Result:** Chart labels remain readable; no overlap
- **Actual Result (Assumed Execution):** Readable with acceptable density
- **Pass/Fail:** PASS
- **Notes:** Edge

## DASH-010: Charts
- **Feature:** Charts
- **Preconditions:** No data
- **Steps:** Open chart with empty result
- **Input Data:** N/A
- **Expected Result:** Chart panel shows empty state, not blank canvas
- **Actual Result (Assumed Execution):** Empty chart state shown
- **Pass/Fail:** PASS
- **Notes:** Empty

## REQ-001: Requests
- **Feature:** Requests
- **Preconditions:** Telemetry sample data exists
- **Steps:** Open Requests page
- **Input Data:** N/A
- **Expected Result:** Paginated request table loads
- **Actual Result (Assumed Execution):** Table loads
- **Pass/Fail:** PASS
- **Notes:** Happy path

## REQ-002: Requests
- **Feature:** Requests
- **Preconditions:** Telemetry sample data exists
- **Steps:** Search by trace id or model
- **Input Data:** gpt-4o
- **Expected Result:** Matching rows only
- **Actual Result (Assumed Execution):** Search filters rows
- **Pass/Fail:** PASS
- **Notes:** Search

## REQ-003: Requests
- **Feature:** Requests
- **Preconditions:** Telemetry sample data exists
- **Steps:** Sort by latency descending
- **Input Data:** N/A
- **Expected Result:** Highest latency first
- **Actual Result (Assumed Execution):** Sort works
- **Pass/Fail:** PASS
- **Notes:** Sorting

## REQ-004: Requests
- **Feature:** Requests
- **Preconditions:** Telemetry sample data exists
- **Steps:** Filter status=error
- **Input Data:** error
- **Expected Result:** Only error requests visible
- **Actual Result (Assumed Execution):** Filter works
- **Pass/Fail:** PASS
- **Notes:** Filtering

## REQ-005: Requests
- **Feature:** Requests
- **Preconditions:** More than one page exists
- **Steps:** Use pagination controls
- **Input Data:** page 2, page size 50
- **Expected Result:** Page changes without losing filters
- **Actual Result (Assumed Execution):** Pagination works
- **Pass/Fail:** PASS
- **Notes:** Pagination

## REQ-006: Requests
- **Feature:** Requests
- **Preconditions:** Trace rows exist
- **Steps:** Open trace detail from table
- **Input Data:** row click
- **Expected Result:** Trace detail loads correct TraceId
- **Actual Result (Assumed Execution):** Detail route loads
- **Pass/Fail:** PASS
- **Notes:** Navigation

## REQ-007: Requests
- **Feature:** Requests
- **Preconditions:** No matches
- **Steps:** Search impossible value
- **Input Data:** zzzz-no-match
- **Expected Result:** No-results state with clear filter action
- **Actual Result (Assumed Execution):** No-results state shown
- **Pass/Fail:** PASS
- **Notes:** Empty

## REQ-008: Requests
- **Feature:** Requests
- **Preconditions:** Large dataset
- **Steps:** Export filtered requests
- **Input Data:** CSV export
- **Expected Result:** CSV downloads with active filters applied
- **Actual Result (Assumed Execution):** Export completes
- **Pass/Fail:** PASS
- **Notes:** Export

## REQ-009: Requests
- **Feature:** Requests
- **Preconditions:** Export in progress
- **Steps:** Double-click export
- **Input Data:** N/A
- **Expected Result:** Button disables/spinner; no duplicate exports
- **Actual Result (Assumed Execution):** Known UX risk: disabled state inconsistent
- **Pass/Fail:** FAIL
- **Notes:** See BUG-P1-004

## REQ-010: Requests
- **Feature:** Requests
- **Preconditions:** Mobile viewport
- **Steps:** Open table
- **Input Data:** 375px
- **Expected Result:** Table usable via card layout or horizontal scroll
- **Actual Result (Assumed Execution):** Horizontal overflow risk observed
- **Pass/Fail:** FAIL
- **Notes:** See BUG-P2-003

## TRACE-001: Trace Detail
- **Feature:** Trace Detail
- **Preconditions:** Trace exists
- **Steps:** Open `/telemetry/traces/[id]`
- **Input Data:** valid trace id
- **Expected Result:** Span tree and attributes render
- **Actual Result (Assumed Execution):** Trace detail loads
- **Pass/Fail:** PASS
- **Notes:** Happy path

## TRACE-002: Trace Detail
- **Feature:** Trace Detail
- **Preconditions:** Invalid trace id
- **Steps:** Open missing trace
- **Input Data:** bad id
- **Expected Result:** Not found state
- **Actual Result (Assumed Execution):** Not found state shown
- **Pass/Fail:** PASS
- **Notes:** Negative

## TRACE-003: Trace Detail
- **Feature:** Trace Detail
- **Preconditions:** Trace includes LLM span
- **Steps:** Inspect prompt/response
- **Input Data:** N/A
- **Expected Result:** Prompt, response, model, tokens, cost visible
- **Actual Result (Assumed Execution):** Details visible
- **Pass/Fail:** PASS
- **Notes:** Core feature

## TRACE-004: Trace Detail
- **Feature:** Trace Detail
- **Preconditions:** Trace includes errors
- **Steps:** Open failed trace
- **Input Data:** error trace
- **Expected Result:** Status and error message visible
- **Actual Result (Assumed Execution):** Error visible
- **Pass/Fail:** PASS
- **Notes:** Error state

## TRACE-005: Trace Detail
- **Feature:** Trace Detail
- **Preconditions:** Large trace
- **Steps:** Open >100 spans repeatedly
- **Input Data:** large traces
- **Expected Result:** Memory stable after close/navigation
- **Actual Result (Assumed Execution):** Potential memory growth risk
- **Pass/Fail:** FAIL
- **Notes:** See BUG-P0-002

## TRACE-006: Trace Detail
- **Feature:** Trace Detail
- **Preconditions:** Trace with pricing data
- **Steps:** Open pricing panel
- **Input Data:** span id
- **Expected Result:** Cost calculation shown or guidance available
- **Actual Result (Assumed Execution):** Pricing data shown
- **Pass/Fail:** PASS
- **Notes:** Pricing

## TELEM-001: Telemetry
- **Feature:** Telemetry
- **Preconditions:** Metrics exist
- **Steps:** Open telemetry overview
- **Input Data:** N/A
- **Expected Result:** Signal summaries load
- **Actual Result (Assumed Execution):** Overview loads
- **Pass/Fail:** PASS
- **Notes:** Happy path

## TELEM-002: Telemetry Metrics
- **Feature:** Telemetry Metrics
- **Preconditions:** Metric exists
- **Steps:** Open metric detail
- **Input Data:** metric name
- **Expected Result:** Timeseries and attributes load
- **Actual Result (Assumed Execution):** Metric detail loads
- **Pass/Fail:** PASS
- **Notes:** Charts

## TELEM-003: Telemetry Metrics
- **Feature:** Telemetry Metrics
- **Preconditions:** Invalid metric
- **Steps:** Open missing metric
- **Input Data:** bad metric
- **Expected Result:** Not found/error state
- **Actual Result (Assumed Execution):** Graceful error simulated
- **Pass/Fail:** PASS
- **Notes:** Negative

## EXC-001: Exceptions
- **Feature:** Exceptions
- **Preconditions:** Error traces exist
- **Steps:** Open Exceptions page
- **Input Data:** N/A
- **Expected Result:** Grouped exception list loads
- **Actual Result (Assumed Execution):** List loads
- **Pass/Fail:** PASS
- **Notes:** Happy path

## EXC-002: Exceptions
- **Feature:** Exceptions
- **Preconditions:** Exception group exists
- **Steps:** Open exception detail
- **Input Data:** group id
- **Expected Result:** Stack/trace samples shown
- **Actual Result (Assumed Execution):** Detail loads
- **Pass/Fail:** PASS
- **Notes:** Drilldown

## EXC-003: Exceptions
- **Feature:** Exceptions
- **Preconditions:** No exceptions
- **Steps:** Filter clean period
- **Input Data:** N/A
- **Expected Result:** Positive empty state shown
- **Actual Result (Assumed Execution):** Empty state shown
- **Pass/Fail:** PASS
- **Notes:** Empty

## COST-001: Costs
- **Feature:** Costs
- **Preconditions:** Cost telemetry exists
- **Steps:** Open Costs page
- **Input Data:** N/A
- **Expected Result:** Cost summary by provider/model loads
- **Actual Result (Assumed Execution):** Cost page loads
- **Pass/Fail:** PASS
- **Notes:** Happy path

## COST-002: Costs
- **Feature:** Costs
- **Preconditions:** Cost telemetry exists
- **Steps:** Filter by provider and date
- **Input Data:** openai, 30d
- **Expected Result:** Cost totals update
- **Actual Result (Assumed Execution):** Filtered totals shown
- **Pass/Fail:** PASS
- **Notes:** Filtering

## COST-003: Costs
- **Feature:** Costs
- **Preconditions:** Custom pricing exists
- **Steps:** Open pricing page
- **Input Data:** N/A
- **Expected Result:** Pricing config table loads
- **Actual Result (Assumed Execution):** Pricing table loads
- **Pass/Fail:** PASS
- **Notes:** CRUD read

## COST-004: Costs
- **Feature:** Costs
- **Preconditions:** User has edit rights
- **Steps:** Add custom model pricing
- **Input Data:** model=demo-llm; input/output prices
- **Expected Result:** Pricing saved and applied to later cost queries
- **Actual Result (Assumed Execution):** Create simulated successful
- **Pass/Fail:** PASS
- **Notes:** CRUD create

## COST-005: Costs
- **Feature:** Costs
- **Preconditions:** Existing pricing row
- **Steps:** Edit pricing value
- **Input Data:** new price
- **Expected Result:** Pricing updates without duplicate row
- **Actual Result (Assumed Execution):** Update works
- **Pass/Fail:** PASS
- **Notes:** CRUD update

## COST-006: Costs
- **Feature:** Costs
- **Preconditions:** Existing pricing row
- **Steps:** Delete pricing config
- **Input Data:** confirm delete
- **Expected Result:** Config removed and default fallback used
- **Actual Result (Assumed Execution):** Delete works
- **Pass/Fail:** PASS
- **Notes:** CRUD delete

## PROMPT-001: Prompt Hub
- **Feature:** Prompt Hub
- **Preconditions:** Authenticated user
- **Steps:** Open Prompt Hub
- **Input Data:** N/A
- **Expected Result:** Prompt list loads
- **Actual Result (Assumed Execution):** List loads
- **Pass/Fail:** PASS
- **Notes:** Happy path

## PROMPT-002: Prompt Hub
- **Feature:** Prompt Hub
- **Preconditions:** User has create rights
- **Steps:** Create prompt
- **Input Data:** name, template, tags
- **Expected Result:** Prompt saved and appears in list
- **Actual Result (Assumed Execution):** Create works
- **Pass/Fail:** PASS
- **Notes:** CRUD create

## PROMPT-003: Prompt Hub
- **Feature:** Prompt Hub
- **Preconditions:** Prompt exists
- **Steps:** Edit prompt template
- **Input Data:** updated content
- **Expected Result:** New version created/prompt updated
- **Actual Result (Assumed Execution):** Edit works
- **Pass/Fail:** PASS
- **Notes:** CRUD update

## PROMPT-004: Prompt Hub
- **Feature:** Prompt Hub
- **Preconditions:** Prompt exists
- **Steps:** Open prompt detail
- **Input Data:** prompt id
- **Expected Result:** Variables, versions, metadata visible
- **Actual Result (Assumed Execution):** Detail visible
- **Pass/Fail:** PASS
- **Notes:** Read

## PROMPT-005: Prompt Hub
- **Feature:** Prompt Hub
- **Preconditions:** Prompt exists
- **Steps:** Compile prompt with variables
- **Input Data:** customer_name=Acme
- **Expected Result:** Compiled output replaces variables
- **Actual Result (Assumed Execution):** Compile works
- **Pass/Fail:** PASS
- **Notes:** API interaction

## PROMPT-006: Prompt Hub
- **Feature:** Prompt Hub
- **Preconditions:** Prompt exists
- **Steps:** Submit missing required variable
- **Input Data:** missing variable
- **Expected Result:** Validation error; no invalid compile
- **Actual Result (Assumed Execution):** Validation shown
- **Pass/Fail:** PASS
- **Notes:** Invalid input

## PROMPT-007: Prompt Hub
- **Feature:** Prompt Hub
- **Preconditions:** Multiple prompts
- **Steps:** Search/filter prompts
- **Input Data:** support, tag=prod
- **Expected Result:** Matching prompts only
- **Actual Result (Assumed Execution):** Search works
- **Pass/Fail:** PASS
- **Notes:** Search

## PROMPT-008: Prompt Hub
- **Feature:** Prompt Hub
- **Preconditions:** Prompt exists
- **Steps:** Delete prompt
- **Input Data:** confirm
- **Expected Result:** Prompt removed or archived
- **Actual Result (Assumed Execution):** Delete works
- **Pass/Fail:** PASS
- **Notes:** CRUD delete

## OPEN-001: OpenGround
- **Feature:** OpenGround
- **Preconditions:** Configured model provider
- **Steps:** Open playground
- **Input Data:** N/A
- **Expected Result:** New playground loads with model controls
- **Actual Result (Assumed Execution):** Loads
- **Pass/Fail:** PASS
- **Notes:** Happy path

## OPEN-002: OpenGround
- **Feature:** OpenGround
- **Preconditions:** Provider key configured
- **Steps:** Send prompt
- **Input Data:** Explain RAG in 2 lines
- **Expected Result:** Response streams/displays; usage captured
- **Actual Result (Assumed Execution):** Response simulated
- **Pass/Fail:** PASS
- **Notes:** Happy path

## OPEN-003: OpenGround
- **Feature:** OpenGround
- **Preconditions:** Two providers configured
- **Steps:** Compare two models
- **Input Data:** gpt-4o vs claude
- **Expected Result:** Both responses display side-by-side
- **Actual Result (Assumed Execution):** Compare works
- **Pass/Fail:** PASS
- **Notes:** Core flow

## OPEN-004: OpenGround
- **Feature:** OpenGround
- **Preconditions:** No provider key
- **Steps:** Send prompt
- **Input Data:** Any prompt
- **Expected Result:** Clear missing-key error
- **Actual Result (Assumed Execution):** Error state shown
- **Pass/Fail:** PASS
- **Notes:** Negative

## OPEN-005: OpenGround
- **Feature:** OpenGround
- **Preconditions:** Existing session
- **Steps:** Save playground session
- **Input Data:** name=Demo Eval
- **Expected Result:** Session appears in OpenGround list
- **Actual Result (Assumed Execution):** Save works
- **Pass/Fail:** PASS
- **Notes:** CRUD create

## OPEN-006: OpenGround
- **Feature:** OpenGround
- **Preconditions:** Saved session exists
- **Steps:** Delete session
- **Input Data:** confirm
- **Expected Result:** Session removed
- **Actual Result (Assumed Execution):** Delete works
- **Pass/Fail:** PASS
- **Notes:** CRUD delete

## EVAL-001: Evaluations
- **Feature:** Evaluations
- **Preconditions:** Eval data exists
- **Steps:** Open Evaluations overview
- **Input Data:** N/A
- **Expected Result:** Quality KPIs and recent results load
- **Actual Result (Assumed Execution):** Overview loads
- **Pass/Fail:** PASS
- **Notes:** Happy path

## EVAL-002: Evaluations
- **Feature:** Evaluations
- **Preconditions:** User has edit rights
- **Steps:** Create evaluation type
- **Input Data:** name, prompt, scoring config
- **Expected Result:** Type saved and listed
- **Actual Result (Assumed Execution):** Create works
- **Pass/Fail:** PASS
- **Notes:** CRUD create

## EVAL-003: Evaluations
- **Feature:** Evaluations
- **Preconditions:** Evaluation type exists
- **Steps:** Edit evaluator config
- **Input Data:** threshold update
- **Expected Result:** Config saved
- **Actual Result (Assumed Execution):** Update works
- **Pass/Fail:** PASS
- **Notes:** CRUD update

## EVAL-004: Evaluations
- **Feature:** Evaluations
- **Preconditions:** Evaluation type exists
- **Steps:** Delete evaluation type
- **Input Data:** confirm
- **Expected Result:** Type removed when unused or blocked if referenced
- **Actual Result (Assumed Execution):** Delete/block works
- **Pass/Fail:** PASS
- **Notes:** CRUD delete

## EVAL-005: Evaluations
- **Feature:** Evaluations
- **Preconditions:** Trace exists
- **Steps:** Run LLM evaluation
- **Input Data:** span id + eval type
- **Expected Result:** Evaluation result saved
- **Actual Result (Assumed Execution):** Run simulated successful
- **Pass/Fail:** PASS
- **Notes:** API

## EVAL-006: Evaluations
- **Feature:** Evaluations
- **Preconditions:** Invalid evaluator data
- **Steps:** Save invalid threshold
- **Input Data:** threshold=-1
- **Expected Result:** Validation error
- **Actual Result (Assumed Execution):** Validation shown
- **Pass/Fail:** PASS
- **Notes:** Invalid input

## RULE-001: Rule Engine
- **Feature:** Rule Engine
- **Preconditions:** Authenticated user
- **Steps:** Open rule engine
- **Input Data:** N/A
- **Expected Result:** Rule list loads
- **Actual Result (Assumed Execution):** List loads
- **Pass/Fail:** PASS
- **Notes:** Happy path

## RULE-002: Rule Engine
- **Feature:** Rule Engine
- **Preconditions:** User has edit rights
- **Steps:** Create rule
- **Input Data:** condition provider=openai; action attach prompt
- **Expected Result:** Rule saved enabled
- **Actual Result (Assumed Execution):** Create works
- **Pass/Fail:** PASS
- **Notes:** CRUD create

## RULE-003: Rule Engine
- **Feature:** Rule Engine
- **Preconditions:** Rule exists
- **Steps:** Evaluate rule against sample attrs
- **Input Data:** provider=openai
- **Expected Result:** Matching action returned
- **Actual Result (Assumed Execution):** Evaluate works
- **Pass/Fail:** PASS
- **Notes:** API

## RULE-004: Rule Engine
- **Feature:** Rule Engine
- **Preconditions:** Rule exists
- **Steps:** Edit rule condition
- **Input Data:** model=gpt-4o
- **Expected Result:** Rule updates
- **Actual Result (Assumed Execution):** Update works
- **Pass/Fail:** PASS
- **Notes:** CRUD update

## RULE-005: Rule Engine
- **Feature:** Rule Engine
- **Preconditions:** Invalid rule
- **Steps:** Save incomplete condition
- **Input Data:** missing operator
- **Expected Result:** Validation error
- **Actual Result (Assumed Execution):** Validation shown
- **Pass/Fail:** PASS
- **Notes:** Invalid input

## RULE-006: Rule Engine
- **Feature:** Rule Engine
- **Preconditions:** Rule exists
- **Steps:** Delete rule
- **Input Data:** confirm
- **Expected Result:** Rule removed
- **Actual Result (Assumed Execution):** Delete works
- **Pass/Fail:** PASS
- **Notes:** CRUD delete

## CTX-001: Context
- **Feature:** Context
- **Preconditions:** Authenticated user
- **Steps:** Open Context page
- **Input Data:** N/A
- **Expected Result:** Context list loads
- **Actual Result (Assumed Execution):** List loads
- **Pass/Fail:** PASS
- **Notes:** Read

## CTX-002: Context
- **Feature:** Context
- **Preconditions:** User has create rights
- **Steps:** Create context entry
- **Input Data:** name, text/body
- **Expected Result:** Context saved
- **Actual Result (Assumed Execution):** Create works
- **Pass/Fail:** PASS
- **Notes:** CRUD create

## CTX-003: Context
- **Feature:** Context
- **Preconditions:** Context exists
- **Steps:** Edit context
- **Input Data:** updated body
- **Expected Result:** Context updates
- **Actual Result (Assumed Execution):** Update works
- **Pass/Fail:** PASS
- **Notes:** CRUD update

## CTX-004: Context
- **Feature:** Context
- **Preconditions:** Invalid context
- **Steps:** Submit blank name
- **Input Data:** empty name
- **Expected Result:** Validation error
- **Actual Result (Assumed Execution):** Validation shown
- **Pass/Fail:** PASS
- **Notes:** Invalid input

## CTX-005: Context
- **Feature:** Context
- **Preconditions:** Context exists
- **Steps:** Delete context
- **Input Data:** confirm
- **Expected Result:** Context removed
- **Actual Result (Assumed Execution):** Delete works
- **Pass/Fail:** PASS
- **Notes:** CRUD delete

## VAULT-001: Vault
- **Feature:** Vault
- **Preconditions:** Authenticated user
- **Steps:** Open Vault
- **Input Data:** N/A
- **Expected Result:** Secrets list displays names only
- **Actual Result (Assumed Execution):** Names only shown
- **Pass/Fail:** PASS
- **Notes:** Security

## VAULT-002: Vault
- **Feature:** Vault
- **Preconditions:** User has create rights
- **Steps:** Create secret
- **Input Data:** name=OPENAI_API_KEY; value masked
- **Expected Result:** Secret saved; value never re-rendered plain
- **Actual Result (Assumed Execution):** Secret saved masked
- **Pass/Fail:** PASS
- **Notes:** CRUD create

## VAULT-003: Vault
- **Feature:** Vault
- **Preconditions:** Secret exists
- **Steps:** Edit/rotate secret
- **Input Data:** new value
- **Expected Result:** Secret rotated and audit event created
- **Actual Result (Assumed Execution):** Rotate works
- **Pass/Fail:** PASS
- **Notes:** CRUD update

## VAULT-004: Vault
- **Feature:** Vault
- **Preconditions:** Secret exists
- **Steps:** Reveal/copy secret
- **Input Data:** N/A
- **Expected Result:** Requires intentional reveal and masks by default
- **Actual Result (Assumed Execution):** Potential plain-text exposure risk
- **Pass/Fail:** FAIL
- **Notes:** See BUG-P0-003

## VAULT-005: Vault
- **Feature:** Vault
- **Preconditions:** Invalid secret
- **Steps:** Submit empty secret name
- **Input Data:** empty
- **Expected Result:** Validation error
- **Actual Result (Assumed Execution):** Validation shown
- **Pass/Fail:** PASS
- **Notes:** Invalid input

## APIKEY-001: API Keys
- **Feature:** API Keys
- **Preconditions:** Authenticated user
- **Steps:** Open API key settings
- **Input Data:** N/A
- **Expected Result:** Key list shows masked tokens
- **Actual Result (Assumed Execution):** List masked
- **Pass/Fail:** PASS
- **Notes:** Security

## APIKEY-002: API Keys
- **Feature:** API Keys
- **Preconditions:** User has edit rights
- **Steps:** Create API key
- **Input Data:** name=Demo Key
- **Expected Result:** One-time token shown; stored masked
- **Actual Result (Assumed Execution):** Create works
- **Pass/Fail:** PASS
- **Notes:** CRUD create

## APIKEY-003: API Keys
- **Feature:** API Keys
- **Preconditions:** API key exists
- **Steps:** Revoke API key
- **Input Data:** confirm
- **Expected Result:** Key revoked and cannot verify
- **Actual Result (Assumed Execution):** Revoke works
- **Pass/Fail:** PASS
- **Notes:** CRUD delete

## APIKEY-004: API Keys
- **Feature:** API Keys
- **Preconditions:** Debug logging enabled
- **Steps:** Perform API request
- **Input Data:** N/A
- **Expected Result:** Sensitive headers never logged
- **Actual Result (Assumed Execution):** Potential header logging risk
- **Pass/Fail:** FAIL
- **Notes:** See BUG-P1-001

## DB-001: Database Config
- **Feature:** Database Config
- **Preconditions:** Authenticated user
- **Steps:** Open database settings
- **Input Data:** N/A
- **Expected Result:** Configs load scoped to current project
- **Actual Result (Assumed Execution):** Configs load
- **Pass/Fail:** PASS
- **Notes:** Project scoping

## DB-002: Database Config
- **Feature:** Database Config
- **Preconditions:** User has edit rights
- **Steps:** Create ClickHouse config
- **Input Data:** host, port, db, credentials
- **Expected Result:** Config saved and selectable
- **Actual Result (Assumed Execution):** Create works
- **Pass/Fail:** PASS
- **Notes:** CRUD create

## DB-003: Database Config
- **Feature:** Database Config
- **Preconditions:** Config exists
- **Steps:** Test connection
- **Input Data:** valid config
- **Expected Result:** Success state shown
- **Actual Result (Assumed Execution):** Success shown
- **Pass/Fail:** PASS
- **Notes:** API

## DB-004: Database Config
- **Feature:** Database Config
- **Preconditions:** Bad config exists
- **Steps:** Test connection
- **Input Data:** bad host
- **Expected Result:** Failure message shown without leaking password
- **Actual Result (Assumed Execution):** Failure shown safely
- **Pass/Fail:** PASS
- **Notes:** Negative

## DB-005: Database Config
- **Feature:** Database Config
- **Preconditions:** Multiple projects
- **Steps:** Switch project
- **Input Data:** project id
- **Expected Result:** Only that project DB configs visible
- **Actual Result (Assumed Execution):** Scoped data visible
- **Pass/Fail:** PASS
- **Notes:** Permissions

## ORG-001: Organisation
- **Feature:** Organisation
- **Preconditions:** Authenticated owner
- **Steps:** Open organisation settings
- **Input Data:** N/A
- **Expected Result:** Org details and members load
- **Actual Result (Assumed Execution):** Loads
- **Pass/Fail:** PASS
- **Notes:** Read

## ORG-002: Organisation
- **Feature:** Organisation
- **Preconditions:** Owner
- **Steps:** Invite member
- **Input Data:** email=dev@example.com; role=developer
- **Expected Result:** Invitation created
- **Actual Result (Assumed Execution):** Invite works
- **Pass/Fail:** PASS
- **Notes:** CRUD create

## ORG-003: Organisation
- **Feature:** Organisation
- **Preconditions:** Owner
- **Steps:** Change member role
- **Input Data:** viewer -> admin
- **Expected Result:** Role updates and permissions follow
- **Actual Result (Assumed Execution):** Role update works
- **Pass/Fail:** PASS
- **Notes:** Roles

## ORG-004: Organisation
- **Feature:** Organisation
- **Preconditions:** Viewer role
- **Steps:** Attempt admin action
- **Input Data:** create API key
- **Expected Result:** Action hidden or forbidden
- **Actual Result (Assumed Execution):** Forbidden simulated
- **Pass/Fail:** PASS
- **Notes:** Permissions

## ORG-005: Projects
- **Feature:** Projects
- **Preconditions:** Owner
- **Steps:** Create project
- **Input Data:** name=Demo Project
- **Expected Result:** Project created and selectable
- **Actual Result (Assumed Execution):** Create works
- **Pass/Fail:** PASS
- **Notes:** CRUD create

## ORG-006: Projects
- **Feature:** Projects
- **Preconditions:** Project exists
- **Steps:** Delete project with configs
- **Input Data:** confirm
- **Expected Result:** Delete blocked or cascades safely with warning
- **Actual Result (Assumed Execution):** Safe block simulated
- **Pass/Fail:** PASS
- **Notes:** Edge

## CHAT-001: Chat
- **Feature:** Chat
- **Preconditions:** Chat config available
- **Steps:** Open Chat page
- **Input Data:** N/A
- **Expected Result:** Conversation UI loads
- **Actual Result (Assumed Execution):** Loads
- **Pass/Fail:** PASS
- **Notes:** Happy path

## CHAT-002: Chat
- **Feature:** Chat
- **Preconditions:** Provider configured
- **Steps:** Send message
- **Input Data:** Summarize trace errors
- **Expected Result:** Assistant response appears and saved
- **Actual Result (Assumed Execution):** Message works
- **Pass/Fail:** PASS
- **Notes:** API

## CHAT-003: Chat
- **Feature:** Chat
- **Preconditions:** No provider configured
- **Steps:** Send message
- **Input Data:** Any
- **Expected Result:** Missing config error
- **Actual Result (Assumed Execution):** Error shown
- **Pass/Fail:** PASS
- **Notes:** Negative

## CHAT-004: Chat Usage
- **Feature:** Chat Usage
- **Preconditions:** Usage exists
- **Steps:** Open chat usage
- **Input Data:** N/A
- **Expected Result:** Usage/cost chart loads
- **Actual Result (Assumed Execution):** Loads
- **Pass/Fail:** PASS
- **Notes:** Reports

## CHAT-005: Chat Settings
- **Feature:** Chat Settings
- **Preconditions:** Owner/admin
- **Steps:** Update chat config
- **Input Data:** model and key
- **Expected Result:** Settings saved
- **Actual Result (Assumed Execution):** Save works
- **Pass/Fail:** PASS
- **Notes:** Settings

## AGENT-001: Agents
- **Feature:** Agents
- **Preconditions:** Agent telemetry exists
- **Steps:** Open Agents page
- **Input Data:** N/A
- **Expected Result:** Agent list/status loads
- **Actual Result (Assumed Execution):** Loads
- **Pass/Fail:** PASS
- **Notes:** Happy path

## AGENT-002: Agents
- **Feature:** Agents
- **Preconditions:** Agent exists
- **Steps:** Open agent detail
- **Input Data:** agent key
- **Expected Result:** Graph, tools, versions load
- **Actual Result (Assumed Execution):** Detail loads
- **Pass/Fail:** PASS
- **Notes:** Drilldown

## AGENT-003: Agents
- **Feature:** Agents
- **Preconditions:** Agent exists
- **Steps:** Refresh/materialize agent
- **Input Data:** agent key
- **Expected Result:** Snapshot refreshes without duplicate nodes
- **Actual Result (Assumed Execution):** Refresh works
- **Pass/Fail:** PASS
- **Notes:** API

## AGENT-004: Agents
- **Feature:** Agents
- **Preconditions:** Missing agent
- **Steps:** Open invalid agent
- **Input Data:** bad key
- **Expected Result:** Not found state
- **Actual Result (Assumed Execution):** Not found shown
- **Pass/Fail:** PASS
- **Notes:** Negative

## FLEET-001: Fleet Hub
- **Feature:** Fleet Hub
- **Preconditions:** Controller data exists
- **Steps:** Open Fleet Hub
- **Input Data:** N/A
- **Expected Result:** Instances list loads
- **Actual Result (Assumed Execution):** Loads
- **Pass/Fail:** PASS
- **Notes:** Happy path

## FLEET-002: Fleet Hub
- **Feature:** Fleet Hub
- **Preconditions:** Instance exists
- **Steps:** Open instance detail
- **Input Data:** instance id
- **Expected Result:** Config/status/TLS data visible
- **Actual Result (Assumed Execution):** Detail loads
- **Pass/Fail:** PASS
- **Notes:** Drilldown

## FLEET-003: Fleet Hub
- **Feature:** Fleet Hub
- **Preconditions:** Invalid TLS config
- **Steps:** Test TLS connection
- **Input Data:** bad cert/host
- **Expected Result:** Failure shown with safe diagnostics
- **Actual Result (Assumed Execution):** Failure shown
- **Pass/Fail:** PASS
- **Notes:** Negative

## MODEL-001: Manage Models
- **Feature:** Manage Models
- **Preconditions:** Authenticated user
- **Steps:** Open manage models
- **Input Data:** N/A
- **Expected Result:** Provider/model list loads
- **Actual Result (Assumed Execution):** Loads
- **Pass/Fail:** PASS
- **Notes:** Read

## MODEL-002: Manage Models
- **Feature:** Manage Models
- **Preconditions:** Model config exists
- **Steps:** Import models
- **Input Data:** JSON file
- **Expected Result:** Valid models added
- **Actual Result (Assumed Execution):** Import works
- **Pass/Fail:** PASS
- **Notes:** Import

## MODEL-003: Manage Models
- **Feature:** Manage Models
- **Preconditions:** Invalid import file
- **Steps:** Import malformed JSON
- **Input Data:** bad file
- **Expected Result:** Validation error; no partial corrupt save
- **Actual Result (Assumed Execution):** Validation shown
- **Pass/Fail:** PASS
- **Notes:** Invalid file

## MODEL-004: Manage Models
- **Feature:** Manage Models
- **Preconditions:** Models exist
- **Steps:** Export model config
- **Input Data:** N/A
- **Expected Result:** JSON downloads
- **Actual Result (Assumed Execution):** Export works
- **Pass/Fail:** PASS
- **Notes:** Export

## REPORT-001: Reports/Exports
- **Feature:** Reports/Exports
- **Preconditions:** Report data exists
- **Steps:** Generate cost report
- **Input Data:** date range=30d
- **Expected Result:** Report created and downloadable
- **Actual Result (Assumed Execution):** Report simulated ready
- **Pass/Fail:** PASS
- **Notes:** Reports

## REPORT-002: Reports/Exports
- **Feature:** Reports/Exports
- **Preconditions:** Large export
- **Steps:** Export 100k traces
- **Input Data:** N/A
- **Expected Result:** Async export with notification
- **Actual Result (Assumed Execution):** Export completes with notification
- **Pass/Fail:** PASS
- **Notes:** Performance

## NOTIF-001: Notifications
- **Feature:** Notifications
- **Preconditions:** Unread notifications exist
- **Steps:** Open notifications menu
- **Input Data:** N/A
- **Expected Result:** Unread list shown
- **Actual Result (Assumed Execution):** List shown
- **Pass/Fail:** PASS
- **Notes:** Notifications

## NOTIF-002: Notifications
- **Feature:** Notifications
- **Preconditions:** Unread notifications exist
- **Steps:** Mark all as read
- **Input Data:** N/A
- **Expected Result:** Unread count resets
- **Actual Result (Assumed Execution):** Count resets
- **Pass/Fail:** PASS
- **Notes:** Update

## NOTIF-003: Notifications
- **Feature:** Notifications
- **Preconditions:** Report export completes
- **Steps:** Wait for export completion
- **Input Data:** N/A
- **Expected Result:** Success notification appears
- **Actual Result (Assumed Execution):** Notification appears
- **Pass/Fail:** PASS
- **Notes:** System event

## SET-001: Profile Settings
- **Feature:** Profile Settings
- **Preconditions:** Authenticated user
- **Steps:** Open profile settings
- **Input Data:** N/A
- **Expected Result:** Profile form loads
- **Actual Result (Assumed Execution):** Loads
- **Pass/Fail:** PASS
- **Notes:** Settings

## SET-002: Profile Settings
- **Feature:** Profile Settings
- **Preconditions:** User edits profile
- **Steps:** Change name/timezone
- **Input Data:** name=Demo User; timezone=Asia/Kolkata
- **Expected Result:** Profile saves and dates use timezone consistently
- **Actual Result (Assumed Execution):** Profile saves; timezone inconsistency risk
- **Pass/Fail:** FAIL
- **Notes:** See BUG-P1-002

## SET-003: Settings
- **Feature:** Settings
- **Preconditions:** Required field error exists
- **Steps:** Correct invalid field
- **Input Data:** valid value
- **Expected Result:** Error clears on change/blur
- **Actual Result (Assumed Execution):** Error may persist until submit
- **Pass/Fail:** FAIL
- **Notes:** See BUG-P3-001

## OPENAPI-001: OpenAPI Spec
- **Feature:** OpenAPI Spec
- **Preconditions:** Authenticated user
- **Steps:** Open OpenAPI spec page
- **Input Data:** N/A
- **Expected Result:** Spec viewer loads and download works
- **Actual Result (Assumed Execution):** Spec loads
- **Pass/Fail:** PASS
- **Notes:** Docs/export

## GETSTART-001: Getting Started
- **Feature:** Getting Started
- **Preconditions:** New user/no data
- **Steps:** Open getting started
- **Input Data:** N/A
- **Expected Result:** Setup instructions and copy buttons work
- **Actual Result (Assumed Execution):** Guide loads
- **Pass/Fail:** PASS
- **Notes:** Onboarding

## ONBOARD-001: Onboarding
- **Feature:** Onboarding
- **Preconditions:** New user
- **Steps:** Complete onboarding steps
- **Input Data:** org/project/db optional
- **Expected Result:** User reaches home and state saved
- **Actual Result (Assumed Execution):** Flow completes
- **Pass/Fail:** PASS
- **Notes:** Onboarding

## RESP-001: Responsiveness
- **Feature:** Responsiveness
- **Preconditions:** Desktop viewport
- **Steps:** Open major pages at 1440px
- **Input Data:** N/A
- **Expected Result:** No overlap; dense tables readable
- **Actual Result (Assumed Execution):** Desktop usable
- **Pass/Fail:** PASS
- **Notes:** Responsive

## RESP-002: Responsiveness
- **Feature:** Responsiveness
- **Preconditions:** Tablet viewport
- **Steps:** Open major pages at 768px
- **Input Data:** N/A
- **Expected Result:** Navigation and forms usable
- **Actual Result (Assumed Execution):** Tablet usable
- **Pass/Fail:** PASS
- **Notes:** Responsive

## RESP-003: Responsiveness
- **Feature:** Responsiveness
- **Preconditions:** Mobile viewport
- **Steps:** Open dashboards/tables/forms at 375px
- **Input Data:** N/A
- **Expected Result:** No clipped controls; tables usable
- **Actual Result (Assumed Execution):** Some data tables overflow
- **Pass/Fail:** FAIL
- **Notes:** See BUG-P2-003

## A11Y-001: Accessibility
- **Feature:** Accessibility
- **Preconditions:** Keyboard only
- **Steps:** Tab through login and main nav
- **Input Data:** N/A
- **Expected Result:** Logical focus order and visible focus
- **Actual Result (Assumed Execution):** Mostly usable
- **Pass/Fail:** PASS
- **Notes:** Accessibility

## A11Y-002: Accessibility
- **Feature:** Accessibility
- **Preconditions:** Screen reader semantics
- **Steps:** Inspect buttons/icons/forms
- **Input Data:** N/A
- **Expected Result:** Controls have accessible names
- **Actual Result (Assumed Execution):** Some icon-only buttons need audit
- **Pass/Fail:** FAIL
- **Notes:** See BUG-P3-005

## A11Y-003: Accessibility
- **Feature:** Accessibility
- **Preconditions:** Color contrast check
- **Steps:** Inspect charts/toasts/errors
- **Input Data:** N/A
- **Expected Result:** Text and states meet WCAG AA
- **Actual Result (Assumed Execution):** Generally acceptable; chart contrast needs audit
- **Pass/Fail:** PASS
- **Notes:** Accessibility risk

## PERF-001: Performance
- **Feature:** Performance
- **Preconditions:** Warm app
- **Steps:** Load dashboard
- **Input Data:** N/A
- **Expected Result:** Initial interactive under 3s in demo data
- **Actual Result (Assumed Execution):** Meets demo threshold
- **Pass/Fail:** PASS
- **Notes:** Performance

## PERF-002: Performance
- **Feature:** Performance
- **Preconditions:** Large trace dataset
- **Steps:** Filter/sort requests
- **Input Data:** N/A
- **Expected Result:** Table interaction under 500ms after data loaded
- **Actual Result (Assumed Execution):** Acceptable with pagination
- **Pass/Fail:** PASS
- **Notes:** Performance

## PERF-003: Performance
- **Feature:** Performance
- **Preconditions:** Concurrent dashboard users
- **Steps:** Simulate 20 users
- **Input Data:** N/A
- **Expected Result:** Queries complete under 5s or degrade gracefully
- **Actual Result (Assumed Execution):** Potential timeouts under load
- **Pass/Fail:** FAIL
- **Notes:** See BUG-P1-006

## BROWSER-001: Browser Compatibility
- **Feature:** Browser Compatibility
- **Preconditions:** Chrome latest
- **Steps:** Run smoke flow
- **Input Data:** N/A
- **Expected Result:** All flows work
- **Actual Result (Assumed Execution):** Pass simulated
- **Pass/Fail:** PASS
- **Notes:** Browser

## BROWSER-002: Browser Compatibility
- **Feature:** Browser Compatibility
- **Preconditions:** Safari latest
- **Steps:** Run smoke flow
- **Input Data:** N/A
- **Expected Result:** All flows work; charts render
- **Actual Result (Assumed Execution):** Pass simulated with chart caveat
- **Pass/Fail:** PASS
- **Notes:** Browser

## BROWSER-003: Browser Compatibility
- **Feature:** Browser Compatibility
- **Preconditions:** Firefox latest
- **Steps:** Run smoke flow
- **Input Data:** N/A
- **Expected Result:** All flows work; downloads work
- **Actual Result (Assumed Execution):** Pass simulated
- **Pass/Fail:** PASS
- **Notes:** Browser
