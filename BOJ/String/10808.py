# Solved on 2022. 6. 6.
# 10808 알파벳 개수

import sys

import sys
import requests
from requests.structures import CaseInsensitiveDict
import time

result = {}

token = "067d658e0b0a9dae53677d11f246aab9b442d5e7e7d6b6681d87096106688b77"

for n in range(111999, 112303):
    try:
        url = "https://api.intra.42.fr/v2/users/" + str(n)

        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer " + token

        resp = requests.get(url, headers=headers).json()
        user_name = resp["login"]
        user_level = resp["cursus_users"][0]["level"]

        # 결과값 저장
        result[user_name] = user_level
        print(n - 111998, end=" : ")
        print(user_name, end=" ")
        print(user_level)
    except:
        print("error T_T")

    time.sleep(0.55)

sorted_dict = sorted(result.items(), key = lambda item: item[1], reverse = True)
for item in sorted_dict:
    print(item[0], end = ' ')
    print(item[1])