BEGIN {
    RS = ""
}

NR == 1 {
    for (i = 1; i <= NF; ++i) {
        if (match($i, /([0-9]+)-([0-9]+)/, arr)) {
            min[i] = arr[1]
            max[i] = arr[2]
        } 
    }
    next
}

NR == 3 {
    for (i = 1; i <= NF; ++i) {
        n = split($i, a, /,/)
        if (n > 1) {
            for (j = 1; j <= n; ++j) {
                valid = 0
                for (m in min) {
                    if (a[j] >= min[m] && a[j] <= max[m]) {
                        valid = 1
                        break
                    } 
                }
                if (!valid) {
                    sum += a[j]
                }
            }
        }
    }
}

END {
    print(sum)
}
