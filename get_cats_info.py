import json

def get_cats_info(file_path):
    result = []

    try: 
        with open(file_path, "r") as file:
            while True: 
                line = file.readline()
                if not line:
                    break
                cat_id, cat_name, cat_age = line.split(",")
                result.append({"id": cat_id, "name": cat_name, "age": int(cat_age)})
    except Exception as e:
        print(f"error {e}")
        print(f"check file {file_path}")
        exit(1)
    return result
    
file_path = "text_files/for_get_cats.txt"
cats = get_cats_info(file_path)
print(json.dumps(cats, indent=4))