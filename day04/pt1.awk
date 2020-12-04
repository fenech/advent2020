BEGIN {
    RS = ""
    FS = "byr|iyr|eyr|hgt|hcl|ecl|pid"
}

NF > 7 { count++ }

END { if (NR) print count + 0 }
