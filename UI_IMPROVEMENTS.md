# UI/UX Improvement Recommendations

## Highest-Impact Demo Polish

1. **Make empty states actionable.** Replace generic no-data messages with setup instructions, clear-filter buttons, and sample-data CTAs.
2. **Improve mobile tables.** Convert wide request, trace, pricing, and member tables to responsive cards or add a column chooser below tablet widths.
3. **Strengthen export feedback.** Use disabled/loading states, progress labels, job notifications, and retry actions for all export/download flows.
4. **Unify settings UX.** Group profile, database, API keys, organisation, evaluation, and chat settings with clearer descriptions and inline success/failure states.
5. **Add global command/search.** `Cmd+K` should navigate pages, find traces/prompts/users, and run common actions.
6. **Standardize timezone formatting.** Use one shared display layer for tables, charts, reports, and exports.
7. **Harden secret handling UI.** Mask by default, require deliberate reveal, auto-hide after seconds, and never copy/show values in logs.
8. **Improve chart accessibility.** Use higher contrast series, persistent legends, keyboard-readable values, and better empty/loading/error states.
9. **Add role-aware affordances.** Hide or disable unavailable actions with concise tooltips explaining required role.
10. **Tighten demo data controls.** Add a visible “Load sample data” admin/dev action for non-production demo environments.

## Unfinished-Looking Areas

- Settings pages feel less polished than dashboard and telemetry pages.
- Empty screens need product-specific next actions.
- File/model import flows need clearer validation summaries.
- Long-running exports need persistent status, not only transient toasts.
- Icon-only actions need labels/tooltips for accessibility and confidence.
