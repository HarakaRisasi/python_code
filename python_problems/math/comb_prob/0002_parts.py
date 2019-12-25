# Standard and non-standard parts.
# one standart part has been seized.
# 21_s and 10_non_s parts. One part has been lost.
# need probability what part has been lost, standart or non_standart.

import subprocess
subprocess.call("clear")

total_parts = 31 - 1
part_st = 21 - 1
part_n_st = 10

def parts(m):
    p = m / total_parts # in percent
    return int(p * 1000) / 10

print(f'{parts(part_st)} % standard part was lost')
#>> 66.6 % standard part was lost

print(f'{parts(part_n_st)} % non-standard part was lost')
#>> 33.3 % non-standard part was lost