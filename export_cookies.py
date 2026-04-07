import json
import pickle

cookies = pickle.load(open("cookies.pkl", "rb"))

with open("cookies.json", "w") as f:
    json.dump(cookies, f)

print("✅ cookies.json created")