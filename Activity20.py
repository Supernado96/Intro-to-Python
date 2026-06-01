wrong_mean = 38
wrong_num = 36
correct_num = 56
total_nums = 40

wrong_sum = wrong_mean*total_nums
print("The wrong sum is", wrong_sum)

correct_sum = wrong_sum - wrong_num +correct_num
print("The correct sum is", correct_sum)

correct_mean = correct_sum/total_nums
print("The correct mean is", correct_mean, "instead of", wrong_mean)