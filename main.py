from pathlib import Path


def total_salary(path):
    path = Path(path)
    total = 0
    count = 0

    if not path.exists():  
        raise FileNotFoundError("File not found")


    if path.exists():
        try:
            with open(path, 'r', encoding='utf-8') as salaries:
                for line in salaries:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
        except Exception as e:
            return f'Error {e}'
    
    average = total // count if count > 0 else 0 
    return total, average
            
total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# ////////////////////////////////////////////////////////

def get_cats_info(path):
    path = Path(path)
    count = 0
    cats_list = []
    
    if not path.exists():  
        raise FileNotFoundError("File not found")

    if path.exists():
        try: 
            with open(path, 'r', encoding='utf-8') as cats:
                for line in cats:
                    id, name, age = line.strip().split(',')
                    cat = {'id': id, 'name': name, 'age': age }
                    cats_list.append(cat)
            return cats_list
        except Exception as e:
            return f'Error {e}'

cats_info = get_cats_info("./cats_file.txt")
print(cats_info)