# Markdown Style Notes

Markdown is designed to be **human-readable source text**. The raw file should make sense even when rendered as plain text, without a Markdown interpreter.

## 1. Readability Comes First

Markdown is not about squeezing content together. It relies on whitespace and structure.

### DO: Create structure with spacing

These two examples render identically, but the first is preferred because it is more easily read as plain text.

```markdown
# Header 1
Markdown paragraphs are separated by a blank line.

## Header 2
This is a second paragraph.

## Header 3
This is a third.
```

Renders the same as:

```markdown
# Header 1
Markdown paragraphs are separated by a blank line.
## Header 2
This is a second paragraph.
## Header 3
This is a third.
```

### DO: Create structure with headers

Use the native header `#` format to create structure:

```markdown
# Main Topic

## Background

Text explaining the background.

## Key Developments

More explanation.
```

Not just bold text:

```markdown
**Main Topic**

**Background**
Text explaining the background.
```

Headers communicate hierarchy. Bold text does not.

## 2. Avoid Inline HTML

Markdown technically allows HTML. You are expected **not** to use it except where explicitly instructed.

HTML violates Markdown's core goal: *readable plain text*.

### DO NOT: Replace Markdown with HTML

This HTML structure is difficult to read:

```markdown
<h2>Section Title</h2>
<ul>
  <li>Item one</li>
  <li>Item two</li>
</ul>
<b>Important term</b>
```

### DO: Use Markdown syntax

The following is equivalent to the above HTML block, but written entirely in Markdown. It is much easier to read as plain text:

```markdown
## Section Title

- Item one
- Item two

**Important term**
```

The HTML version is harder to scan, harder to edit, and defeats the purpose of Markdown.

## 3. Write for Humans First, Renderers Second

Assume your Markdown file may be:

- Viewed raw on GitHub
- Read in a code editor
- Copied into another system

If it only looks good after rendering, it is not written correctly.
