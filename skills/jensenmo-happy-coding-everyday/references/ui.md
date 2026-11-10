# UI guide

For any change that adds or alters a screen, a component, or interface text. The repository's design rules and narrower UI standard skills come first; everything here is a default.

## Stack

Use the stack the project already has. When there is none yet, pick the simplest one that fits the request and what the user says they use, and name it in one line of your reply unless the user does not program; a single page often needs only HTML, CSS, and a little script. Do not add a framework, build tool, CSS framework, component library, or CDN dependency unless the request needs it or the user asks.

## Two kinds of page

- **Working screens** (tools, forms, dashboards, admin, settings): keep them plain and quiet. The next three sections apply as written.
- **Pages meant to make an impression** (a business home page, landing page, portfolio, event page), or any request that asks for the result to look good: design it properly, following "Designed pages" below. A plain utility look under-delivers here.

## When the product already has a look

- Reuse its components, tokens, spacing, type scale, layout, and navigation, and match the density and alignment of neighboring screens. Do not add arbitrary colors, fonts, radii, shadows, or a second component library. When you need something the product lacks, such as an error color, reuse its nearest existing token instead of adding one.

## When there is nothing to copy

A first page still has to look deliberate. Do not leave browser defaults.

- **Layout:** let the content decide the structure. Put what people look for first at the top, group related things, left-align text, and right-align numbers in columns. Cap the page width and keep lines of text to a comfortable reading length.
- **Spacing:** use one scale (for example multiples of 4 or 8 px) everywhere, with more space between groups than inside them. Prefer whitespace to boxes and rules.
- **Type:** the system font stack, two or three sizes, two weights, body text of at least 14 px, and line height around 1.5.
- **Color:** dark text on a light neutral background, one accent for the primary action and links, and one color for errors. Use grey only for secondary text and keep its contrast readable (at least 4.5:1). Define these once as variables.
- **Controls:** native elements with a comfortable click area, one primary button per view, and visible focus, hover, and disabled states.
- **Tables and lists:** a header row, consistent alignment per column, and a deliberate choice to wrap or truncate long values.
- **Narrow screens:** nothing overflows the page sideways; a wide table may scroll inside its own container.

## Decoration

On a working screen, unless the project already uses them or the user asks, leave out: decorative gradients, glows, or glass effects; emoji or icons used as decoration; a hero, banner, or illustration; a card around every block; oversized radii and stacked shadows; pill badges and "New" or "Pro" labels; placeholder statistics, testimonials, or logos; centered marketing layouts; and motion that does not show a change of state.

## Designed pages

Use your full design ability; these points keep it honest.

- **Start from the subject:** what it is, who visits, and what feeling fits. Let that choose the typefaces, colors, and layout, not a default style.
- **Type:** pair a display face with a text face from fonts already on people's devices (serif and sans-serif stacks) or font files in the project. Make headings large and confident, with a clear scale down to body text.
- **Color:** a small palette with character taken from the subject: one dominant color and one or two supporting ones, checked for readable contrast.
- **Layout:** compose it. Give the first screen a strong focus, vary the rhythm between sections, use generous space, and align to a grid. Avoid a stack of identical centered blocks.
- **Images:** draw them in CSS or SVG, generate them and save them inside the project when you have an image tool, or leave clearly labelled placeholders. Say in your reply which you did. Do not link to photos on other sites.
- **Details:** hover and focus states, careful spacing, and motion only where it helps.
- **Still required:** every word comes from the user's content, with nothing invented (no testimonials, awards, statistics, or history); it works on a phone; no framework unless the request needs one. Avoid the stock marks of generated pages: purple-to-blue gradients, glass panels, emoji as icons, rows of icon cards, and filler such as "Welcome to".

## Headings and text

- One title per page. Add a heading only when it names a group that people need to find among other groups. No heading over a single item, no subtitle that restates the title, no small label above a title, and no filler headings such as "Overview" or "Details". When the navigation item, page title, and panel title would say the same thing, keep one.
- Write interface text in the words the product already uses: short, specific, and calm, with no hype, exclamation marks, filler, jargon, or invented terms. Give each thing one name, in the interface's language, everywhere it appears: navigation, page title, labels, buttons, and messages.
- Say each thing once: no helper text that restates its label, no message shown in two places, and no counts or summaries nobody asked for. Add helper text only where people would otherwise make a mistake. Keep notes for developers off the page: caveats about unfinished parts, where data is stored ("saved in this browser"), disclaimers, and "please note" text belong in your report, including inside success and error messages. Use real labels and data shapes; when real content is missing, use neutral placeholders and mention them in the report.

## Scope and states

- Build only the screens, controls, and states the task needs: no extra buttons such as Cancel or Reset. Ask before adding settings, sections, or variants (such as a dark theme) that nobody requested.
- Handle the loading, empty, and error states the change introduces, in plain text, without decorative empty-state art.
- Keep controls accessible: labels tied to inputs, keyboard access, and native elements before custom widgets.
- Do not hand-edit generated API clients; change the contract and regenerate them. Keep type checking meaningful: do not silence errors with `any`, casts, or suppression comments.

## Check

Look at the result. Open it in a browser when one is available, at desktop and phone width, and step through the states you changed; widen the check when shared or global styles change. When you cannot view it, say so and check the structure instead. Make sure it works the way the user will open it (as a file, through the project's server, or after a build), and give that exact step in your reply.
