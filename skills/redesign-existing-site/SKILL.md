---
name: redesign-existing-site
description: Redesign an existing website's visual system and page templates using product-appropriate personality, hierarchy, spacing, typography, color, depth, imagery, and finishing tactics while preserving required content and behavior. Use only when the user explicitly asks for a redesign or broad visual transformation, not routine polish or token cleanup.
---

# Redesign Existing Site

Apply the practical design principles associated with *Refactoring UI* as a transformation workflow, not as a generic aesthetic. Preserve what the site does while replacing weak or inconsistent visual decisions with a coherent system suited to the site's audience, stakes, and subject.

## Define what may change

Before implementation, distinguish invariants from redesign scope:

- Preserve routes, working behavior, data flow, required content, analytics hooks, accessibility semantics, and business rules unless the user authorizes changes.
- Treat information architecture, copy, brand assets, and interaction patterns as changeable only when the request includes them.
- Allow layout, visual hierarchy, typography, spacing, color, radius, borders, elevation, imagery treatment, and component styling to change substantially.
- Follow repository conventions and retain the established framework unless replacement is explicitly requested.

If the request is only to polish a screen while retaining its visual direction, use an incremental UI-refactoring workflow instead. If the request is only to consolidate existing CSS values without changing the design, use a token-normalization workflow.

## Audit the current site

- Inventory representative page types, shared shells, component families, responsive states, and important user flows.
- Render representative wide and narrow states. Record the current strengths as well as the failures; redesign does not require discarding every existing choice.
- Identify the site's primary job, audiences, trust requirements, content density, and the consequences of user error.
- Rank structural problems before surface problems: unclear priorities, weak grouping, unsuitable density, and inconsistent component behavior come before decorative polish.

## Establish the new personality

Read [references/personality-to-system.md](references/personality-to-system.md) for every redesign. Produce a short personality profile and visual thesis before styling broadly. Translate that thesis into coordinated decisions for type, palette, radius, borders, shadows, spacing, imagery, icons, and copy tone.

Do not map an industry directly to a fashionable look. An insurance site may need precision and trust, but its audience might still benefit from warmth and modest rounding. Explain how the chosen visual signals support the product rather than citing the category as the sole reason.

## Redesign a representative feature first

Choose a high-value page or flow that exercises the site's real content, controls, actions, feedback, and repeated components. Redesign that vertical slice before the global shell or every page. This exposes whether the proposed personality and token system work under realistic conditions.

Read [references/redesign-principles.md](references/redesign-principles.md) while developing the representative feature. Define a compact system of primitive and semantic tokens from the decisions demonstrated there. Avoid speculative tokens that have no current consumer.

For a large site, treat the representative slice as a checkpoint unless the user explicitly asks for an autonomous end-to-end redesign. Resolve evident weaknesses in the direction before multiplying it across templates.

## Carry the system across the site

When implementation is authorized, read [references/migration-and-qa.md](references/migration-and-qa.md). Migrate shared foundations and components before page-specific overrides. Work in coherent batches so visual regressions remain attributable.

- Replace duplicated visual rules with semantic tokens and shared primitives.
- Preserve deliberate page differences that follow content or task needs.
- Include hover, active, focus, selected, disabled, loading, empty, error, and success states that the product can enter.
- Keep responsive layouts task-led; do not merely compress the desktop composition.
- Avoid unrelated behavioral refactors during the visual migration.

## Verify the redesign

Compare renders at identical viewport sizes against both the old baseline and the new visual thesis. Confirm:

- the screen's purpose and primary action are immediately legible;
- related content groups clearly and reading order remains sound;
- the personality is expressed consistently rather than through radius alone;
- text, contrast, focus, target size, imagery, overflow, and responsive states remain accessible;
- shared pages look related without becoming mechanically identical;
- the implementation uses the new system instead of accumulating replacement literals.

Finish with the personality thesis, major system decisions, transformed scope, preserved invariants, and verification evidence.
