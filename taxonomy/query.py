import lmdb

db_path = "./taxonomy_directory"

env = lmdb.open(db_path, readonly=True)

while True:
    key = input("Enter the scientific name or 'q' to quit: ").strip()
    
    if key == 'q':
        break
    
    with env.begin() as txn:
        common_name = txn.get(key.encode())
        
        if common_name:
            print(f"Common Name: {common_name.decode()}")
        else:
            print("Entry not found.")

env.close()
