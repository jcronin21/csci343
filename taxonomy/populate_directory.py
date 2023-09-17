import lmdb

# Path to LMDB database directory
db_path = "./taxonomy_directory"

# Path to CSV file
csv_file = "species.csv"

# Open the LMDB environment
env = lmdb.open(db_path, map_size=104857600) 

# Open the LMDB database
with env.begin(write=True) as txn:
    with open(csv_file, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            if len(parts) == 2:
                scientific_names = parts[0].split(' ')
                #gets rid of characters that are not letters
                common_name = parts[1].strip('"')

                key = '/'.join(scientific_names)
                txn.put(key.encode(), common_name.encode())
env.close()
