BEGIN { RS = "" }

match($0, /byr:([0-9]+)/, arr) && arr[1] >= 1920 && arr[1] <= 2002 &&
match($0, /iyr:([0-9]+)/, arr) && arr[1] >= 2010 && arr[1] <= 2020 &&
match($0, /eyr:([0-9]+)/, arr) && arr[1] >= 2020 && arr[1] <= 2030 &&
((match($0, /hgt:([0-9]{3})cm/, arr) && arr[1] >= 150 && arr[1] <= 193) ||
    (match($0, /hgt:([0-9]{2})in/, arr) && arr[1] >= 59 && arr[1] <= 76)) &&
/hcl:#[0-9a-f]{6}\y/ &&
/ecl:(amb|blu|brn|gry|grn|hzl|oth)\y/ &&
/pid:[0-9]{9}\y/ {
    count++
}

END { if (NR) print count + 0 }
