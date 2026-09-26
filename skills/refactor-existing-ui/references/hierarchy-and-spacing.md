# Hierarchy and spacing

Use this reference to distinguish structural problems from cosmetic ones.

## Attention order

Assign each visible element a role before styling it:

- **Primary:** the content or action that fulfills the screen's job.
- **Supporting:** information needed to interpret or complete the primary task.
- **Contextual:** metadata, secondary actions, and optional detail.

Use more than size to express these roles. Weight, contrast, color, placement, and surrounding space can change prominence without creating oversized text or controls. De-emphasize contextual material instead of continuously amplifying primary material.

Do not let visual prominence damage document structure. Keep semantic heading levels and accessible names correct even when their visual treatments differ.

Labels are useful when a value would otherwise be ambiguous. Prefer recognizable formatting, grouping, or concise inline context when a permanent label merely repeats what the value already communicates.

## Grouping and spacing

Spacing communicates relationships. An element should sit visibly closer to the content it belongs with than to the next group. Treat equal gaps around a label, heading, error, or control as suspicious when they make ownership ambiguous.

Start a correction with generous separation between major groups, then tighten related elements. Derive values from the project's spacing scale; if no scale exists, use a small progression with enough contrast between adjacent steps to be perceptible.

Size containers from their content and task. A wide viewport does not require stretched controls, long lines, or edge-to-edge content. Use maximum widths where additional width harms scanning or comprehension.

Use grids when repeated content needs shared alignment, not as an automatic page skeleton. Prefer local alignment rules for asymmetric or content-led layouts. Align text and icons optically, including baselines, rather than relying on identical bounding-box centers.

## Common diagnoses

| Symptom | Likely cause | First correction to try |
| --- | --- | --- |
| Everything feels equally loud | No explicit attention order | Reduce contrast or weight of supporting and contextual elements |
| A screen feels cramped despite small content | Major and minor gaps are too similar | Increase separation between groups before changing component padding |
| A form is hard to scan | Labels, help, errors, and controls do not form clear units | Make within-field gaps smaller than between-field gaps |
| Content floats in a large viewport | Containers expand without a content reason | Add a defensible max-width and intentional placement |
| Many boxes compete visually | Boundaries substitute for grouping | Replace some borders with space or surface contrast |

Treat these as diagnostic prompts, not automatic transformations. The rendered context decides whether a correction is appropriate.
