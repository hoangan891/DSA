def online_insertion(arr, stream):
    for val in stream:
        arr.append(val)
        key = val
        j = len(arr) - 2
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)

arr = []
stream_inputs = [5, 2, 8, 1]
online_insertion(arr, stream_inputs)