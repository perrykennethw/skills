---
name: build-ui-foundations
description: Define a coherent visual foundation and reusable design tokens for a new or early-stage web interface. Use when a user needs a visual direction, typography, spacing, color, radius, border, or elevation system before detailed component styling. Do not use for polishing an established interface or producing an entire page design by itself.
---

# Build UI Foundations

Create a bounded visual decision system that makes later interface work faster and more consistent. Stop at foundations unless the user also asks for components or screens to be built.

## Ground the system

Identify:

- the product's subject, audience, and primary task;
- existing brand assets or constraints;
- the desired personality and density;
- the target platforms and styling stack;
- accessibility, localization, and theming requirements that affect tokens.

When information is missing, make a conservative, clearly stated assumption and proceed. Do not invent a rebrand when usable brand direction already exists.

Read [references/foundation-decisions.md](references/foundation-decisions.md) when choosing the visual direction and primitive scales. Read [references/token-contract.md](references/token-contract.md) when mapping decisions into CSS variables, Tailwind configuration, theme objects, or another implementation format.

## Start from a representative feature

Choose one realistic, high-value feature that exercises headings, body text, controls, actions, surfaces, and states. Use it to test foundation decisions. Avoid designing a generic application shell first; navigation chrome alone rarely exposes whether the system supports the product's real content.

## Define a compact system

Create only the choices the product presently needs:

- a type family strategy and finite type roles;
- a spacing and sizing progression with visibly distinct steps;
- neutral, action, accent, and feedback color roles with necessary states;
- border, radius, and elevation decisions tied to the chosen personality;
- content widths and density rules where they improve readability or scanning.

Separate primitive values from semantic roles. Components should consume semantic roles such as `text-muted` or `surface-raised`, not raw palette positions. Add component-specific tokens only when a component has a stable exception that cannot be expressed semantically.

Do not add dark mode, multiple themes, motion scales, or extensive component tokens unless the request or existing product requires them.

## Deliver usable foundations

Return or implement:

1. A short visual thesis connecting the choices to the product
2. Primitive scales and semantic assignments
3. The requested framework representation
4. A small representative example showing the tokens working together
5. Constraints, assumptions, and accessibility checks

If editing a repository, follow its naming and file conventions. Prefer extending an existing token mechanism over installing a competing one.

## Validate

Render the representative feature at wide and narrow widths. Confirm that the system creates a clear hierarchy, distinguishable spacing levels, readable text, sufficient state contrast, and a consistent surface model. Revise the foundation when the example requires many arbitrary exceptions; repeated exceptions usually indicate that a primitive scale or semantic role is missing or poorly chosen.
