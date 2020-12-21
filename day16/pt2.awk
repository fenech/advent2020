BEGIN {
    RS = ""
    FS = "\n"
    result = 1
}

NR == 1 {
    for (i = 1; i <= NF; ++i) {
        n = split($i, a, /: |or |-/)
        field = a[1]
        for (j = 2; j <= n; j += 2) {
            min[field,j] = a[j]
            max[field,j] = a[j+1]
        }
    }
}

NR == 2 {
    split($2, my_ticket, /,/)  
}

NR == 3 {
    for (i = 2; i <= NF; ++i) {
        n = split($i, ticket, /,/)
        for (j = 1; j <= n; ++j) {
            for (m in min) {
                if (ticket[j] >= min[m] && ticket[j] <= max[m]) {
                    name = substr(m, 0, index(m, SUBSEP))
                    valid[i][j][name]
                }
            }
        }

        if (length(valid[i]) == n) {
            print "valid:", $i
        } else {
            print "invalid:", $i
            delete valid[i]
        }
    }

    valid_tickets = length(valid)
    print valid_tickets, "valid,", NF - 1 - valid_tickets, "invalid"

    for (i in valid) {
        for (j in valid[i]) {
            for (m in valid[i][j]) {
                possible[m][j]++
            }
        }
    }

    for (m in possible) {
        print m
        for (j in possible[m]) {
            if (possible[m][j] == valid_tickets) {
                print j
            }
            else delete possible[m][j]
        }
        print ""
    }

    found_options = 1
    while (found_options) {
        found_options = 0
        for (m in possible) {
            options = length(possible[m])
            if (options == 1) {
                found_options = 1
                for (choice in possible[m]) {
                    print m, choice
                    if (m ~ /^departure/) {
                        result *= my_ticket[choice]
                    }
                    for (p in possible) {
                        delete possible[p][choice]   
                    }
                }
            } 
        }
    }
}

END {
    if (NR) {
        print "result:", result
    }
}
