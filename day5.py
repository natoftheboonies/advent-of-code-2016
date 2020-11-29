from hashlib import md5
from itertools import count

SAMPLE_INPUT = "abc"
PUZZLE_INPUT = "ugkcyxxp"

result = ""
result2 = ["_"] * 8

for s in count(1):
    x = md5((PUZZLE_INPUT + str(s)).encode())
    if x.hexdigest().startswith("00000"):
        digest = x.hexdigest()
        c5 = digest[5]
        if len(result) < 8:
            result += c5
        if c5.isdigit() and int(c5) < 8 and result2[int(c5)] == "_":
            result2[int(c5)] = digest[6]
            # print (''.join(result2))
        if "_" not in result2:
            print(f"evaluted {s} hashes")
            break

print("#1", result)
print("#2", "".join(result2))
