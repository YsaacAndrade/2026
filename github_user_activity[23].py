import requests
import sys


def main():


    print(recent_activity(confirm_request(get_request(get_url(clean_username(get_username()))))))


def get_username():
    return input("What's your username? ")


def clean_username(user_input):
    while True:
        user_input = user_input.strip()

        if (user_input.startswith("-")) or (user_input.endswith("-")):
            print("Please, insert a valid username.")
            user_input = input("What's your username? ")

        else:
            return user_input


def get_url(user):
    return f"https://api.github.com/users/{user}/events"


def get_request(url):
    return requests.get(url)


def confirm_request(request):
    if request.status_code == 200:
        return request.json()

    else:
        sys.exit("Something went wrong! :(")

def recent_activity(confirmed_request):
    event_type = confirmed_request[0]["type"]
    repo = confirmed_request[0]["repo"]["name"]
    return f"Your most recent event is a {event_type} in {repo}"


if __name__ == "__main__":
    main()