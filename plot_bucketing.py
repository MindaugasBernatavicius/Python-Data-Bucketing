import matplotlib.pyplot as plt
import numpy as np
import re
import math as m

### VARIABLE DEFINITIONS
filename = "data"
times = []

### PREPARE DATA: PUSH TO LISTS
file = open(filename, "r")
for line in file:
   # print(line, end ='')
   ts = re.search('(?:\[\s{0,})(\d.+?)(?:\.)', line).group(1)
   times.append(ts)
file.close()

### BUCKETING LOGIC
# I need to spet through the buckets and see if the TS belongs in that bucket
# that is why I need to know how many buckets there will be
bucketing_coefficient = 1                                     # every 100 seconds we will have an aggregation bucket
bucket_count = m.ceil(int(times[-1]) / bucketing_coefficient)   # since we have an ordered list, we know that max is last
buckets = []                                                    # we will hold the bucket names here
event_counts_per_bucket = []                                    # event count that happened in the duration of each bucket

### CUMULATIVE
bucket_index = 1                                                # used to multiply bucketing_coefficient to obtain the next bucket
for bucket in range(bucket_count):
    events_count_for_this_bucket = 0
    for time in times:
        if int(time) < (bucketing_coefficient * bucket_index):
            events_count_for_this_bucket = events_count_for_this_bucket + 1
        else:
            event_counts_per_bucket.append(events_count_for_this_bucket)
            buckets.append(bucket * bucketing_coefficient)
            bucket_index = bucket_index + 1
            break

### NON-CUMULATIVE
# bucket_index = 1                                                # used to multiply bucketing_coefficient to obtain the next bucket
# time_idx = 0
# for bucket in range(bucket_count):
#     events_count_for_this_bucket = 0
#     for time in range(time_idx, len(times)):
#         if int(times[time]) < (bucketing_coefficient * bucket_index):
#             print(times[time])
#             events_count_for_this_bucket = events_count_for_this_bucket + 1
#             time_idx = time_idx + 1
#         else:
#             event_counts_per_bucket.append(events_count_for_this_bucket)
#             buckets.append(bucket * bucketing_coefficient)
#             bucket_index = bucket_index + 1
#             break

plt.plot(buckets, event_counts_per_bucket)
# plt.xticks(np.arange(min(events), max(events)+1, 20.0))
plt.show()

#plt.plot([0,1,2,3], [0.6,0.8,12,15])
#plt.show()
