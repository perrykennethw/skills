# Token contract

## Layers

Use the fewest layers that preserve meaning:

1. **Primitives** store reusable raw values, such as palette steps or spacing values.
2. **Semantic tokens** express interface roles, such as `color-text-muted`, `space-section`, or `shadow-overlay`.
3. **Component tokens** encode justified stable exceptions, such as a specialized chart or editor surface.

Components should normally consume semantic tokens. Avoid exposing primitive names as the public contract when a future theme or brand adjustment would need to reinterpret them.

## Naming

- Name by role, not current appearance: prefer `surface-selected` to `blue-100` at the semantic layer.
- Keep direction consistent: either `color-text-muted` or `text-color-muted`, not both.
- Use state suffixes consistently for hover, active, focus, disabled, and selected.
- Do not place implementation-specific terms such as `hex` or `px` in token names.

## Framework mapping

For CSS custom properties, place stable semantic tokens at the narrowest shared scope that supports them. Theme overrides should change semantic assignments rather than force component selectors to know about themes.

For Tailwind, extend the existing theme and map utilities to semantic variables when the project already uses them. Do not replace familiar project utilities with a custom plugin merely to enforce naming.

For JavaScript or TypeScript theme objects, preserve type safety and the consuming library's expected shape. Avoid maintaining a second hand-synchronized source when tokens can be generated or imported from one canonical file.

## Required documentation in the result

Show enough context for another developer to use the system:

- the visual role of each semantic group;
- foreground/background pairs;
- state relationships;
- one representative usage example;
- intentional exceptions and unsupported themes.

Do not generate a large token catalog with no demonstrated consumer.
