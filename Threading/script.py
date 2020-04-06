import concurrent.futures
import threading
import time

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping {seconds} second(s)...'

start = time.perf_counter()

# old way of threading
# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} second(s)...')

# new way of threading

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    
    # using submit method
    results = [executor.submit(do_something, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

    # using map method
    # results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)...')