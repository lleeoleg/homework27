"""
HW 26
"""
import time
import requests

def func(urls):
    """_summary_

    Args:
        urls (_type_): _description_
    """
    for url in urls:
        print(requests.get(url))
def main():
    """_summary_
    """
    urls = ["http://example.com"] * 100
    start_time = time.time()
    func(urls)
    end_time = time.time()
    print(f"Время затрачено: {end_time - start_time} секунд")

if __name__ == "__main__":
    main()
