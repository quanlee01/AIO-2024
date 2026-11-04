def max_in_k_window(list, k):
    window = []
    answer = [] 
    for i, num in enumerate(list): 
        if window and window[0] < i - k + 1: 
            window.pop(0)
        while window and list[window[-1]] < num: 
            window.pop()
        window.append(i)
        if i >= k - 1: 
            answer.append(list[window[0]])
    return answer
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1] 
k = 3 
print(max_in_k_window(num_list, k))