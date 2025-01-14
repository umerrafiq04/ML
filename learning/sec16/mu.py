# import multiprocessing
# import time

# def sq():
#     for i in range(10):
#         time.sleep(1)
#         print(f"square: {i*i}", flush=True)

# def cb():
#     for i in range(10):
#         time.sleep(1)
#         print(f"cube: {i*i*i}", flush=True)

# # create 2 processes
# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=sq)    
#     p2 = multiprocessing.Process(target=cb) 

#     t = time.time()

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     ft = time.time() - t
#     print(f"time = {ft:.2f} seconds")


from concurrent.futures import ProcessPoolExecutor
import time

def square(nums):
    time.sleep(1)
    return f"square:{nums*nums}"

numbers=[1,2,3,4,5,6,7,8,9]
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square,numbers)

    for result in results:
        print(result)