params = {"accuracy": 90, 
          "epochs": 12,
            "optimaizer": "adam"
         }

while params:
    key,value = params.popitem()
    print(f"removed: {key} - {value}")
