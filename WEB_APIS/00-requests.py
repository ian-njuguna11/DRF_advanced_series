import imp
from urllib import response


import requests

def main():
    # response = requests.get("http://www.google.com/random")
    response = requests.get("http://www.google.com")
    print("Status code: ", response.status_code)
    print("Content: ", response.text)
    # print("Headers: ", response.headers)
    # print("Content-Type: ", response.headers['Content-Type'])
    # print("Content type: ", response.)


if __name__ == "__main__":
    main()
