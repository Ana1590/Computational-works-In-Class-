import time    

def insertion_sort(data):
    j = 1
    for j in range(j, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] =data[i]
            i = i - 1
        data[i + 1] = key
    

unsorted_cards = list(range(1,10))
unsorted_cards.sort(reverse = True)
start = time.time()
insertion_sort(unsorted_cards)
sum = 0
sum = sum + (time.time() - start)
print("sorting 10 cards took ", sum , "seconds" )

unsorted_cards = list(range(1,100))
unsorted_cards.sort(reverse = True)
start = time.time()
insertion_sort(unsorted_cards)
sum = 0
sum = sum + (time.time() - start)
print("sorting 100 cards took " , sum , "seconds")

unsorted_cards = list(range(1,1000))
unsorted_cards.sort(reverse = True)
start = time.time()
insertion_sort(unsorted_cards)
print("sorting 1000 cards took ", sum, "seconds")

unsorted_cards = list(range(1,10000))
unsorted_cards.sort(reverse = True)
start = time.time()
insertion_sort(unsorted_cards)
sum = 0
sum = sum + (time.time() - start)
print("sorting 10000 cards took ", sum , "seconds")
