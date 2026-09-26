# Foundation decisions

## Visual thesis

Describe the visual direction in operational terms rather than mood-board adjectives alone. Resolve a few useful tensions:

- restrained or expressive;
- dense or spacious;
- soft or crisp;
- quiet or high-contrast;
- familiar or distinctive.

Connect each choice to the audience and task. A dense operations tool and a narrative marketing experience can share a brand while needing different layout and type behavior.

## Typography

Choose typefaces by role and available assets. A single family with a useful weight range is often enough for an application. Distinct display and reading faces are justified when the content or brand benefits from the contrast.

Define named roles before raw values: display, page title, section title, body, compact body, label, and caption are common candidates, not mandatory slots. Keep the scale compact. Specify size, line height, weight, and letter spacing together so consuming code does not reconstruct the decision.

Set readable measures for prose and help text. Data tables, dashboards, and code-oriented views may use width differently and should not inherit article constraints blindly.

## Spacing and sizing

Choose a small progression whose adjacent steps are perceptibly different. Include enough small values for control internals and enough large values for section separation. Name primitives numerically or neutrally; express purpose through semantic aliases where the stack supports them.

Avoid deriving every dimension from one ratio. Icon sizes, tap targets, text measures, and layout widths solve different problems even when they share underlying values.

## Color

Define neutral and brand families with sufficient range for foregrounds, surfaces, borders, and interaction states. Treat success, warning, and danger as semantic communication colors rather than decoration.

For each semantic background, identify its expected foreground, border, focus, hover, and selected roles. Verify real pairs instead of declaring a palette "accessible" in isolation. Provide a non-color signal for meaningful states.

## Shape and elevation

Radius and shadow choices should reinforce the visual thesis. Limit the number of levels. Define elevation by relationship—base, raised, overlay—rather than by a catalog of decorative shadow recipes.

Use borders, background shifts, or spacing for separation when elevation would imply the wrong interaction or physical relationship.

## Test composition

The representative feature should contain enough variety to reveal weaknesses: a title, supporting text, primary and secondary actions, a form or control, a repeated content group, a feedback state, and at least two surface levels. It is a test fixture for the system, not a mandatory production component.
