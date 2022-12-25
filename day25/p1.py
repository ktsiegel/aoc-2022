from sys import argv
from math import log, ceil


def get_max(place):
    total = 0
    for i in range(0, place):
        total += 2*5**i
    return total

def main(filename):
    # Read the input file
    with open(filename, "r") as f:
        input = [x.strip() for x in f.readlines()]

    digits = {
        "2": 2,
        "1": 1,
        "0": 0,
        "-": -1,
        "=": -2
    }

    ans = 0
    for l in input:
        total = 0
        for index in range(len(l)-1, -1, -1):
            place = len(l)-index-1
            digit = l[index]
            to_add = (5**place)*digits[digit]
            total += to_add
        ans += total

    ans_digits = int(ceil(log(ans)/log(5)))
    snafu_ans = ""
    for i in range(ans_digits):
        place = ans_digits-i-1
        bound = get_max(place)
        if ans >= -1*bound and ans <= bound:
            snafu_ans += "0"
        elif ans < 0:
            # want to land in between -5**(place-1) and 5**(place-1)
            if ans+5**place >= -1*bound and ans+5**place <= bound:
                snafu_ans += "-"
                ans += 5**place
            else:
                snafu_ans += "="
                ans += 5**place*2
        elif ans-5**(place) >= -1*bound and ans-5**(place) <= bound:
            snafu_ans += "1"
            ans -= (5**place)
        else:
            snafu_ans += "2"
            ans -= 2*5**place
    
    print(snafu_ans, ans)

        




if __name__ == "__main__":
    main(argv[1])

        