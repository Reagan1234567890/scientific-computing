def dataintake(d):
    return input(f"[+] Enter {d} and split using commas: ")

def printer(data_dict):
    print("""
    --------------------------------------
    | Data          | Type      | Conversion |
    --------------------------------------
    """)
    for key, value in data_dict.items():
        print(f"    {key:<12} | {value['type']:<10} | {value['conversion']}")

def main():
    intake = True
    while intake:
        try:
            integer = list(map(int, dataintake('integers').split(',')))
            floats = list(map(float, dataintake('floats').split(',')))
            list_data = dataintake('list').split(',')
            tuple_data = tuple(dataintake('tuple').split(','))
            b = input("Are you a boy or a girl? true or false: ").strip().lower() == 'true'
            extra = set(dataintake('sets').split(','))

            data_dict = {
                "Integers": {"type": str(type(integer)), "conversion": str(list(map(float, integer)))},
                "Floats": {"type": str(type(floats)), "conversion": str(list(map(int, floats)))},
                "List": {"type": str(type(list_data)), "conversion": "N/A"},
                "Tuple": {"type": str(type(tuple_data)), "conversion": "N/A"},
                "Boolean": {"type": str(type(b)), "conversion": "N/A"},
                "Set": {"type": str(type(extra)), "conversion": "N/A"},
            }
            
            printer(data_dict)
            intake = False
            
        except ValueError:
            print("[!] Invalid input. Please enter the correct format.")
            continue

if __name__ == "__main__":
    main()
