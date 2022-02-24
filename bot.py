import requests
import os
import json

from dotenv import load_dotenv
config = load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "ReactRT bot"
    return r


# def get_rules():
#     response = requests.get(
#         "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
#     )
#     if response.status_code != 200:
#         raise Exception(
#             "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
#         )
#     print(json.dumps(response.json()))
#     return response.json()


# def delete_all_rules(rules):
#     if rules is None or "data" not in rules:
#         return None

#     ids = list(map(lambda rule: rule["id"], rules["data"]))
#     payload = {"delete": {"ids": ids}}
#     response = requests.post(
#         "https://api.twitter.com/2/tweets/search/stream/rules",
#         auth=bearer_oauth,
#         json=payload
#     )
#     if response.status_code != 200:
#         raise Exception(
#             "Cannot delete rules (HTTP {}): {}".format(
#                 response.status_code, response.text
#             )
#         )
#     print(json.dumps(response.json()))


def set_rules(delete):
    # You can adjust the rules if needed
    query_rules = [
        {"value": "(#React OR #ReactJS) -is:retweet"}
    ]
    payload = {"add": query_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(set):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            data = (json_response['data'])
            id = data['id']
            print(data, id)

            # payload = {"tweet_id": id}
            # retweet = requests.post(
            #     f"https://api.twitter.com/2/users/2763492627/retweets/",
            #     auth=bearer_oauth,
            #     json=payload
            # )
            # print(retweet.status_code)
            # if retweet.status_code != 201:
            #     raise Exception(
            #         "Cannot retweet"
            #     )
            # print(f"Retweeted tweet with {id}")

def main():
    get_stream(set)


if __name__ == "__main__":
    main()