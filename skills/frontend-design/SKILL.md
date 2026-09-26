---
name: frontend-design
description: Design and build distinctive, production-quality frontends with intentional art direction, typography, layout, motion, and interface copy. Use when Codex creates a new web UI, landing page, application screen, interactive experience, or materially reshapes an existing frontend and the result should avoid generic template aesthetics.
---

# Frontend Design

> Adapted for Codex from Anthropic's `frontend-design` skill and modified for Codex workflows in July 2026. See `LICENSE.txt`.

Act as the design lead at a small studio known for giving each client a recognizable visual identity. Make deliberate choices specific to the brief. Take one defensible aesthetic risk and execute it well.

## Ground the direction in the subject

- Identify the concrete subject, audience, and interface's single primary job before designing.
- If the brief leaves these unclear, choose sensible specifics, state the assumption briefly, and continue.
- Draw visual language from the subject's materials, tools, artifacts, history, and vernacular.
- Use the user's real content and repository context. Do not fill the finished interface with generic placeholder copy when credible content can be written.
- Honor explicit visual direction exactly. Treat the brief as the source of truth.

## Form a compact design thesis

Plan these elements before implementation:

1. **Color:** Define 4–6 named color tokens with hex values and clear roles.
2. **Type:** Choose distinct display and body roles; add a utility role for captions or data only when useful. Set an intentional scale, weight range, width, and spacing.
3. **Layout:** Describe the composition in one or two sentences. Use a visual sketch or rendered preview when comparison would materially help; do not substitute decorative diagrams for design judgment.
4. **Signature:** Name the single element the experience should be remembered by.
5. **Motion:** Choose one orchestrated motion idea, or explicitly choose restraint. Respect reduced-motion preferences.
6. **Copy:** Establish the audience, register, and vocabulary the interface will use.

For web pages, make the hero a thesis: lead with the most characteristic thing in the subject's world, whether that is a line of copy, image, live demonstration, interaction, or unusual composition.

## Reject unearned defaults

Interrogate every free design choice. Common patterns can be appropriate, but require a reason grounded in the subject. Watch especially for:

- warm cream, high-contrast serif, and terracotta used as automatic "taste";
- near-black with one acid accent used as automatic "tech";
- broadsheet grids, hairline rules, and zero-radius cards used as automatic "editorial";
- gradient-backed metric cards presented as a universal hero;
- numbered sections where the content is not actually sequential;
- arbitrary glows, glass panels, pills, oversized rounded cards, and scattered micro-animation.

Review the design thesis against the brief. If any choice could be dropped unchanged into several unrelated projects, revise it. Spend boldness in one place and keep the supporting system disciplined.

## Build from the approved thesis

- Preserve the repository's framework, conventions, and working behavior unless the task explicitly calls for replacement.
- Derive implementation tokens from the design thesis. Avoid ad hoc colors, spacing, radii, and type rules.
- Let structure encode meaning. Use labels, dividers, numbering, and grouping only when they clarify relationships.
- Match execution complexity to the direction. Maximalism requires layered craft; minimalism requires exact spacing, type, rhythm, and detail.
- Keep CSS selectors predictable and low-specificity. Check for conflicting class, element, and responsive rules.
- Build responsive behavior deliberately rather than shrinking a desktop composition.
- Provide visible keyboard focus, semantic controls, useful alternative text, sufficient contrast, and reduced-motion handling.
- Treat loading, empty, error, and success states as part of the design when the product can enter them.

## Write interface copy as design material

- Write from the user's side of the screen. Name what people recognize and control, not implementation details.
- Use active voice, plain verbs, sentence case, and specific language.
- Name an action consistently throughout a flow: a **Publish** button should lead to a **Published** confirmation.
- Make controls describe their outcome: prefer **Save changes** to **Submit**.
- Explain errors concretely and give the next corrective action. Do not apologize or use vague failure language.
- Turn empty states into clear invitations to act.
- Give each text element one job: a label labels, an example demonstrates, and helper text helps.

## Critique the rendered result

Inspect the actual interface, preferably through screenshots or the running application, at desktop and mobile sizes.

Check:

- whether the subject and primary job are immediately legible;
- whether the signature element is memorable without competing decoration;
- typography hierarchy, line length, wrapping, rhythm, and density;
- alignment, overflow, breakpoint behavior, and touch targets;
- hover, focus, active, loading, empty, error, and reduced-motion states;
- whether any element feels borrowed from a generic template rather than earned by the brief.

Remove at least one nonessential flourish before finishing. Re-render after meaningful revisions and report the implemented direction and verification concisely.
