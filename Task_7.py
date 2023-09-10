import asyncio
import random

async def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        result_rnd = await asyncio.gather(
            fib(n - 1),
            asyncio.sleep(random.uniform(0, 1))
        )
        result_nrm = await asyncio.gather(
            fib(n - 2)
        )
        return result_rnd[0] + result_nrm[0]

async def main():
    try: #Added to make it type safe. Not mentioned in the task.
        in_user = int(input("Enter a positive number: "))
    
        if in_user <= 0:
            print("Please enter a positive number.")
            return
        if in_user >=10: # Not mentioned in the task, put it for informative purpose
            print(f"The return of the function will take more than 10 seconds. Bigger Numbers result in more waiting time")   

        taskList = [fib(in_user - 1), fib(in_user - 2)]
        out_compute = await asyncio.gather(*taskList)

        print(f"Fib({in_user}) = {sum(out_compute)}")
    
        first_done = out_compute.index(min(out_compute))
    
        if first_done == 0:
            print("Task 1 was calculated first")
        elif first_done == 1:
            print("Task 2 was calculated first")
    
    except ValueError:
        print("Invalid input. Enter a positive integer.")

if __name__ == "__main__": #Best practice?
    asyncio.run(main())