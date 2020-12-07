BEGIN {
  RS = ""
  FS = ""
}

{
  delete(a)
  for (i = 1; i <= NF; ++i)
    if ($i ~ /[a-z]/) a[$i]
  count += length(a)
}

END { if (NR) print count }
