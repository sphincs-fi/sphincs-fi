#!/usr/bin/env python3
import attack
import sys
seed = 0
success = 0
for attempt in range(1,10000):
    # 1 = success
    # -1 = failure 
    _, rc = attack.attack("wotsp_faulty_sigmas.txt", 20, 1, seed)
    if rc == 1:
        success += 1;
    print(f"{success}/{attempt} ({success/attempt});")
    sys.stdout.flush()
    seed += 1
