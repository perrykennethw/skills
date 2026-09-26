# States and visual verification

## State inventory

Inspect only states the component or flow can actually enter. Common candidates are:

- initial and populated;
- hover, active, keyboard focus, selected, and disabled;
- loading, partial loading, and stale data;
- empty, filtered-empty, and first-use;
- inline validation, recoverable error, and terminal error;
- success or confirmation;
- long labels, localized copy, missing images, and large user values.

An empty state should explain the situation and present the next useful action when one exists. Errors should remain associated with the affected control or operation. Disabled states must stay legible and should not be used when an explanation or validation message would serve the user better.

## Visual comparison

Keep the baseline and revised screenshots at identical viewport dimensions. Compare in this order:

1. Can a new viewer identify the screen's purpose and primary action?
2. Are related items visibly grouped and major sections distinct?
3. Does the reading path work without decorative cues?
4. Are dense areas still scannable and sparse areas still intentional?
5. Do responsive changes preserve priority instead of merely compressing the desktop layout?

Inspect at least one narrow and one wide state when the interface is responsive. Add intermediate viewports when wrapping, grids, sidebars, or overlays change behavior there.

## Completion threshold

Stop when the ranked structural issues are resolved, the revised render is visibly clearer, and relevant behavioral checks pass. Do not keep adding polish merely to make the change set feel substantial. Record deliberate exceptions when the product, brand, or technical constraints justify them.
