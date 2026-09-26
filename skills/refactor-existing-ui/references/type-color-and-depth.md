# Type, color, depth, and imagery

Read only the sections relevant to the observed problems.

## Typography

- Build hierarchy from a limited type scale. Before adding a new size, test a change in weight, contrast, case, or spacing.
- Choose line height in relation to font size and measure: smaller text and longer lines generally need more leading; large display text usually needs less.
- Keep prose at a readable measure. Let dense data interfaces use width differently from articles or explanatory copy.
- Align text by its baseline when neighboring labels, values, and icons otherwise appear uneven.
- Use letter spacing deliberately. Large headings may benefit from tighter spacing; small uppercase text often needs more room.
- Links need a reliable affordance, but color is not the only option. Context, underline, weight, and interaction states can carry the role.

## Color

Assign colors to roles rather than components: canvas, surface, primary text, muted text, border, action, accent, success, warning, and danger. A usable family normally needs enough light and dark steps to support tinted surfaces, interactive states, borders, and readable foregrounds.

Do not manufacture muted text by selecting an arbitrary gray for every background. On colored surfaces, derive a foreground that belongs to the same visual environment and verify its contrast against the actual composited background.

Maintain the character of a hue as its lightness changes. When creating a new scale, use a perceptual color space such as OKLCH when the target stack supports it; otherwise inspect every shade rather than assuming a numerical interpolation will look even.

Never make color the only carrier of state or meaning. Pair it with text, iconography, shape, position, or another persistent cue. Check contrast for text, controls, focus indicators, and meaningful graphics.

## Boundaries and depth

Use the lightest mechanism that communicates separation:

1. Space when proximity is enough
2. Background contrast when regions need definition
3. A border when the edge itself matters
4. A shadow when elevation or overlap matters

Shadows should imply one coherent lighting environment. Higher surfaces may use broader and softer shadows; nearby surfaces usually need tighter shadows. Avoid making every container appear raised.

Overlaps can communicate layers or connect sections, but they create responsive and clipping risks. Verify them at narrow widths, increased text size, and with dynamic content.

## Imagery

- Give images a deliberate display size and crop behavior. Do not rely on a source file's intrinsic dimensions.
- Test user-provided images with extreme aspect ratios, low resolution, transparency, and missing content.
- When text overlays imagery, create stable contrast with a scrim, gradient, crop choice, or separate text surface. Test against both very light and very dark images.
- Preserve subject visibility across breakpoints by adjusting focal position or composition instead of shrinking the desktop crop blindly.
