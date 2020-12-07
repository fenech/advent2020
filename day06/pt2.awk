BEGIN {
  RS = ""
  FS = "\n"
}

{
  delete(a)

  for (i = 1; i <= NF; ++i) {
    n = split($i, chars, //)
    for (j = 1; j <= n; ++j) {
      c = chars[j]
      a[c]++
    }
  }

  for (c in a) {
    if (a[c] == NF)
      count++
  }
}

END { if (NR) print count }
