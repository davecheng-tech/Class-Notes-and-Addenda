#set page(
  width: 20cm,
  height: auto,
  margin: (x: 1cm, y: 1cm),
)

#set text(font: "New Computer Modern", size: 10.5pt)

#let prime-col = rgb("#f0f0f0")
#let bar-col   = rgb("#ffffff")
#let head-fill = rgb("#2c2c2c")
#let row-alt   = rgb("#f8f8f8")

#let p(x) = $#x$   // plain math shorthand

#table(
  columns: (5.5cm, 6cm, 6cm),
  inset: (x: 10pt, y: 8pt),
  align: (left, left, left),

  // Header
  table.header(
    table.cell(fill: head-fill, text(fill: white, weight: "bold")[Law]),
    table.cell(fill: head-fill, text(fill: white, weight: "bold")[Prime ( $'$ ) notation]),
    table.cell(fill: head-fill, text(fill: white, weight: "bold")[Overbar notation]),
  ),

  // Identity
  table.cell(fill: row-alt)[*Identity*],
  $ A + 0 = A \ A dot 1 = A $,
  $ A + 0 = A \ A dot 1 = A $,

  // Null / Domination
  [*Null / Domination*],
  $ A + 1 = 1 \ A dot 0 = 0 $,
  $ A + 1 = 1 \ A dot 0 = 0 $,

  // Idempotent
  table.cell(fill: row-alt)[*Idempotent*],
  $ A + A = A \ A dot A = A $,
  $ A + A = A \ A dot A = A $,

  // Complement
  [*Complement*],
  $ A + A' = 1 \ A dot A' = 0 $,
  $ A + overline(A) = 1 \ A dot overline(A) = 0 $,

  // Double Negation
  table.cell(fill: row-alt)[*Double Negation*],
  $ (A')' = A $,
  $ overline(overline(A)) = A $,

  // Commutative
  [*Commutative*],
  $ A + B = B + A \ A dot B = B dot A $,
  $ A + B = B + A \ A dot B = B dot A $,

  // Associative
  table.cell(fill: row-alt)[*Associative*],
  $ (A+B)+C = A+(B+C) \ (A dot B) dot C = A dot (B dot C) $,
  $ (A+B)+C = A+(B+C) \ (A dot B) dot C = A dot (B dot C) $,

  // Distributive
  [*Distributive*],
  $ A dot (B+C) = A B + A C \ A + (B C) = (A+B)(A+C) $,
  $ A dot (B+C) = A B + A C \ A + (B C) = (A+B)(A+C) $,

  // Absorption
  table.cell(fill: row-alt)[*Absorption*],
  $ A + A B = A \ A dot (A+B) = A $,
  $ A + A B = A \ A dot (A+B) = A $,

  // De Morgan's
  [*De Morgan's*],
  $ (A dot B)' = A' + B' \ (A + B)' = A' dot B' $,
  $ overline(A dot B) = overline(A) + overline(B) \ overline(A + B) = overline(A) dot overline(B) $,

  // XOR Identity
  table.cell(fill: row-alt)[*XOR Identity*],
  $ A'B + A B' = A xor B $,
  $ overline(A) B + A overline(B) = A xor B $,
)
