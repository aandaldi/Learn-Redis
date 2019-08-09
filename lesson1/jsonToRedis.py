import json
import redis
from pprint import pprint

client = redis.Redis()


restaurant_484272 = {
    "name": "Ravagh",
    "type": "Persian",
    "address": {
        "street": {
            "line1": "11 E 30th St",
            "line2": "APT 1",
        },
        "city": "New York",
        "state": "NY",
        "zip": 10016,
    }
}
## JSON TO REDIS
client.set(484272, json.dumps(restaurant_484272))

print(restaurant_484272)
print('=========')
pprint(json.loads(client.get(484272)))