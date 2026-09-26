# Migration and visual QA

## Migration order

Prefer this dependency order when it fits the repository:

1. Global primitives: fonts, color families, spacing, size, radius, and elevation values
2. Semantic roles: text, surfaces, boundaries, actions, feedback, and states
3. Shared controls and content primitives
4. Navigation and page shells
5. Representative page templates
6. Specialized pages and justified exceptions

Do not perform a blind global replacement. The same literal may serve unrelated roles, and two near-duplicate literals may need to remain distinct.

Keep each batch renderable. When the current and new systems must coexist temporarily, define the scope explicitly and remove the bridge only after all intended consumers have migrated.

## Baseline matrix

Capture a proportionate set of evidence before changing shared styles:

- one wide and one narrow viewport for each representative template;
- important navigation and overlay states;
- forms with validation and long content;
- data-heavy, empty, loading, error, and success states where present;
- light and dark themes only when the site supports both.

## Visual review

Compare old and new renders at identical viewport sizes. The new result need not be pixel-similar, but it must preserve required content and behavior. Check:

- purpose, reading path, and action priority;
- grouping and spacing ownership;
- text wrapping, truncation, measure, and baseline alignment;
- overflow, responsive reflow, sticky elements, and overlays;
- contrast, visible keyboard focus, control names, and target sizes;
- image crops, missing media, and dynamic content;
- personality consistency across shared and specialized pages.

## Behavioral checks

Run the repository's relevant tests, build, type checks, and focused interaction checks. Pay special attention to selectors, DOM changes, or component substitutions that may affect scripts, analytics, automated tests, forms, or routing.

## Completion threshold

Finish when the authorized page set uses the new semantic system, the representative state matrix has been inspected, relevant automated checks pass, and any retained old styles or deliberate exceptions are documented. Do not extend the redesign into product behavior or information architecture without explicit scope.
