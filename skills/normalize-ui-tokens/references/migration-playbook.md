# Token migration playbook

## Classify before naming

For each frequent value, inspect representative usages and answer:

- Is it content foreground, surface, boundary, action, feedback, spacing, type, shape, or elevation?
- Does the value change by theme, state, breakpoint, or component scope?
- Is its similarity to another value intentional or accidental?
- Would changing both usages together in the future be desirable?

Only values that should change together belong behind the same semantic token.

## Suggested migration order

1. Adopt or extend the canonical token file.
2. Add primitives needed by demonstrated semantic roles.
3. Add semantic aliases with clear foreground/background and state relationships.
4. Replace exact duplicate usages in a bounded area.
5. Render and compare that area.
6. Consider near-duplicate consolidation after its visual impact is understood.
7. Remove superseded definitions only after no consumers remain.

This order is a risk-management pattern, not a required commit structure.

## Common traps

- **Tokenizing syntax:** `gray-500` describes a palette coordinate; `text-muted` describes why a component uses it. Keep those layers distinct.
- **One token per literal:** this renames inconsistency instead of reducing it.
- **One universal spacing token:** identical values can play unrelated roles that may diverge later.
- **Premature component tokens:** repeated semantic roles usually belong at the semantic layer.
- **Global replacement:** the same text can occur inside unrelated themes, media queries, charts, or third-party overrides.
- **Visual drift hidden by cleanup:** formatting and structural refactors make before/after comparisons noisy.

## Verification evidence

Use the strongest evidence available in the repository:

- screenshot or visual-regression comparisons;
- computed-style checks for critical states;
- component stories or preview routes;
- theme and responsive snapshots;
- targeted unit tests for token resolution when the styling system is programmatic.

Pixel identity is appropriate for a preservation migration. When the user explicitly authorizes consolidation of near-duplicates, document the intentional differences and verify that hierarchy, contrast, and state recognition remain sound.
