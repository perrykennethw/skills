---
name: normalize-ui-tokens
description: Audit an existing frontend for repeated or near-duplicate visual values, define a coherent token model, and migrate usages incrementally without unnecessary visual change. Use for hard-coded CSS cleanup, Tailwind theme consolidation, or design-token normalization. Do not use to choose a new visual direction or redesign the interface.
---

# Normalize UI Tokens

Turn accidental repetition into an explicit visual system while preserving the current interface. Tokenization is successful when values become easier to reason about and change, not when every literal is mechanically replaced.

## Establish scope and baseline

- Read repository guidance and locate existing theme files, CSS variables, framework configuration, component libraries, and generated styles.
- Confirm whether the user wants an audit, a proposed migration, or implementation. Do not modify files for an audit-only request.
- Capture representative rendered states or existing visual tests before migrating values.
- Exclude vendored, generated, compiled, and third-party code from both analysis and edits.

Run `scripts/audit_style_literals.py <path>` for a first-pass inventory when the source format is supported. Use `--json` when another process will consume the results. Treat the output as evidence to investigate, not as a list of automatic replacements.

Read [references/migration-playbook.md](references/migration-playbook.md) before deciding which values to merge or when implementing a migration.

## Build the token model

Inventory existing values and group them by actual role and usage context. Distinguish:

- exact duplicates that express the same decision;
- near-duplicates that may be accidental;
- visually similar values with different semantic roles;
- legitimate one-off values tied to media, data visualization, or geometry.

Prefer a small layered model:

1. Primitive palette and scale values where reuse is real
2. Semantic roles consumed across components
3. Component-specific tokens only for stable, justified exceptions

Do not merge values based on numerical proximity alone. Two close colors may need separate semantics; two distant values may represent states in the same semantic family.

## Migrate incrementally

- Extend the repository's current token mechanism rather than introducing a parallel architecture.
- Begin with high-frequency, low-risk exact duplicates.
- Migrate one semantic family or component boundary at a time.
- Preserve cascade behavior, responsive overrides, theme scopes, state specificity, and runtime-computed values.
- Avoid unrelated formatting or component refactors that make visual regressions harder to isolate.
- Record intentional literals or exceptions instead of forcing them into misleading tokens.

## Verify

After each meaningful batch, run the relevant tests and compare computed or rendered output at representative viewports and states. Check light/dark themes only when they exist. Inspect hover, focus, selected, disabled, feedback, and overlay states affected by the migrated tokens.

Finish with the token model introduced, migrated scope, deliberate exceptions, and verification performed. If the inventory reveals inconsistent art direction rather than accidental literals, stop and recommend a separate foundations or design decision before normalizing it away.
