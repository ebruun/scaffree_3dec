import itasca as it
import json

it.command("python-reset-state false")

it.command("model restore 'Final_State'")

a = it.history.get("1","2")

print(a)