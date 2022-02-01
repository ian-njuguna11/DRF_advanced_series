
import requests

def main():
    url = "http://api.exchangeratesapi.io/v1/latest?access_key=c34316a336f10e947c977cc631da3071"
    response = requests.get(url)

    if response.status_code != 200 :
        print("Status code: ", response.status_code)
        raise Exception("There was an error")

    # print("Content-Type: ", response.headers['Content-Type'])
    print("Json: ", response.json())

if __name__ == "__main__":
    main()