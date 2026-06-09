import time

#add the retry logic to the API call
#add timeout to the API call
for attempt in range(3):

    try:
        response = api_call()
        break

    except Exception:
        wait_time = 2 ** attempt
        print(f"Retrying in {wait_time}s")
        time.sleep(wait_time)