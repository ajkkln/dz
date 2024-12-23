import json
def serialize(data, path):
    with open(path, 'w', encoding='utf-8') as file:
        records = []
        for record in data:
            record_str = ', '.join(f"{key}: {value}" for key, value in record.items())
            records.append(record_str)
        
        file.write('; '.join(records) + '\n')


def deserialize(path):
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        records = content.split('; ')
        
        data = []
        for record in records:
         
            record_dict = {}
            pairs = record.split(', ')
            for pair in pairs:
                key, value = pair.split(': ', 1)  
                
                if value.isdigit():
                    value = int(value)
                elif value.startswith('"') and value.endswith('"'):
                    value = value[1:-1] 
                record_dict[key] = value
            data.append(record_dict)
        
        return data


data_to_serialize = [
    {"id": 1, "name": "Иван Петров", "age": 35, "has_altushka": 0},
    {"id": 2, "name": "Петр Сидоров", "age": 48, "has_altushka": 1}
]
serialize(data_to_serialize, 'data.txt')
loaded_data = deserialize('data.txt')
print(loaded_data)
