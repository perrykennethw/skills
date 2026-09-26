# Redesign principles

Use these principles to turn the personality thesis into an interface. Diagnose the content before choosing a treatment.

## Start with the feature

Design around the page's real task and content before perfecting navigation or an application shell. Begin at useful fidelity: establish structure and priority before icons, decorative detail, or exhaustive states. Do not design more page types than the current decision requires.

## Limit choices

Define compact, reusable scales for type, spacing, color, radius, and elevation. A constrained system makes intentional exceptions visible. Create tokens from demonstrated needs rather than generating a large theoretical catalog.

## Make hierarchy explicit

Assign visible content to primary, supporting, or contextual roles. Use combinations of weight, contrast, color, placement, and space instead of making every important element larger. De-emphasize metadata and secondary actions so primary content can lead.

Keep semantic document structure correct even when the visual order uses different treatments. Remove labels only when formatting or context makes the value unambiguous.

## Use spacing to encode relationships

Related elements should be closer to each other than to neighboring groups. Start with generous separation between major regions, then tighten internal relationships. Avoid ambiguous equal gaps that make headings, errors, labels, or actions appear attached to the wrong content.

Size layouts from the task. Use readable maximum widths and content-led alignment instead of stretching everything to fill the viewport or forcing every page onto the same grid.

## Design text as a system

Use a limited type scale and specify size, weight, line height, and tracking together. Set line length for the content type. Align neighboring text and icons optically, including baselines. Make links recognizable through the combination of context, decoration, color, and interaction state rather than color alone.

## Give color roles

Create enough neutral and brand steps for foregrounds, surfaces, borders, interaction states, and tinted feedback. Assign semantic roles such as canvas, surface, text, muted text, action, selected, success, warning, and danger. Verify actual foreground/background pairs and provide a non-color cue for meaningful state.

## Create depth intentionally

Use the lightest separation mechanism that communicates the relationship: space, background contrast, border, then elevation. Shadows should imply a coherent light source and surface hierarchy. Do not make every region a card or every card float.

## Treat imagery as variable content

Define aspect ratio, crop, focal position, and fallback behavior. Test light and dark images behind text, extreme user-uploaded aspect ratios, missing media, transparency, and small sources. Use a scrim, gradient, or separate surface when text contrast cannot otherwise remain stable.

## Finish the real states

Make native-looking defaults deliberate. Design the empty, loading, validation, error, success, focus, hover, selected, and disabled states that the flow can actually reach. Use decoration to reinforce the personality after the structure works, not to conceal weak hierarchy.
