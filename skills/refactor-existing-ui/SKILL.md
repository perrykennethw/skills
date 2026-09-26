---
name: refactor-existing-ui
description: Diagnose and improve an existing web interface through incremental visual refactoring while preserving its behavior, product structure, and established brand direction. Use when a user asks to polish, clean up, professionalize, or fix a page or component that "looks off." Do not use for a greenfield interface or a major rebrand.
---

# Refactor Existing UI

Treat the work as a visual refactor: retain the interface's purpose and working behavior while making its hierarchy and relationships easier to perceive. Prefer a few high-leverage corrections over a blanket restyle.

## Establish the baseline

- Read the repository instructions and identify the rendering stack, styling conventions, reusable components, and existing design tokens.
- Inspect the actual rendered interface when possible. Capture representative wide and narrow states before editing so visual changes can be compared against a stable baseline.
- State the screen's primary job and the intended first, second, and third points of attention. Infer these from the product and content rather than from the current styling alone.
- Preserve the user's content, brand assets, framework, and interaction model unless the request explicitly changes them.

If the user requests only a critique or diagnosis, report findings without modifying files.

## Diagnose by impact

Rank observed problems by how much they obscure meaning or impair use. Start with structure and finish with decoration:

1. Attention order and action priority
2. Grouping, alignment, density, and ambiguous spacing
3. Type hierarchy, readability, and text alignment
4. Color roles, contrast, and non-color affordances
5. Boundaries, depth, imagery, and surface treatment
6. Empty, loading, error, success, hover, focus, and disabled states

Read [references/hierarchy-and-spacing.md](references/hierarchy-and-spacing.md) when attention order, grouping, alignment, or density is involved. Read [references/type-color-and-depth.md](references/type-color-and-depth.md) when type, palette, surfaces, shadows, or imagery needs work. Read [references/states-and-verification.md](references/states-and-verification.md) for state coverage and visual QA.

## Implement the smallest coherent correction

- Address root causes before symptoms. Fix a weak hierarchy or confused grouping before adding decoration.
- Remove unnecessary visual signals before introducing new ones. Space, alignment, background contrast, and type treatment can often replace borders or containers.
- Reuse existing tokens and components where they express the intended role. Introduce a new token only when the value represents a repeatable decision.
- Preserve semantic HTML, keyboard behavior, accessible names, focus visibility, and information conveyed without color.
- Keep changes locally consistent: a new heading treatment, spacing relationship, or surface rule should apply to the equivalent elements in scope.
- Do not silently change product behavior, information architecture, copy meaning, or application state.

## Verify the result

Render the changed interface at representative wide and narrow viewports. Compare it with the baseline and check:

- the primary job and action are apparent without scanning every element;
- adjacent elements look more related than unrelated elements;
- text wraps, truncates, and aligns intentionally;
- contrast, focus, overflow, touch targets, and responsive behavior remain sound;
- relevant empty and failure states still work;
- the improvement comes from clearer decisions rather than more decoration.

Iterate when the rendered evidence exposes a regression. Finish with a concise account of the design problems corrected and the states or viewports verified.
