#!/usr/bin/env python
import json

def weight_load(cur_reps, weight, desired_reps):
    rep_map = [100, 95, 93, 90, 87, 83, 80, 77, 75, 70]
    if not (cur_reps >= 1 and cur_reps <= 10):
        raise ValueError("reps must be between 1 and 10 inclusive")
    if not (desired_reps >= 1 and desired_reps <= 10):
        raise ValueError("desired reps must be between 1 and 10 inclusive")
    
    percentage_of_single = rep_map[cur_reps-1]
    single_rep_max = weight/(percentage_of_single/100)
    return dict(
        percentage=percentage_of_single,
        single=int(single_rep_max),
        desired_weight=int(single_rep_max*(rep_map[desired_reps-1]/100))
    )

if __name__ == '__main__':
    from optparse import OptionParser
    p = OptionParser()
    p.add_option("--weight", type="int")
    p.add_option("--reps", type="int")
    p.add_option("--desired-reps", type="int")
    opt, arg = p.parse_args()
    print(
        json.dumps(
            weight_load(opt.reps, opt.weight, opt.desired_reps),
            separators=(',', ':'),
            indent=4,
            sort_keys=True
        )
    )