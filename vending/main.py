def run(input_file: str, output_file: str) -> None:
    with open(input_file) as f:
        operations = f.read()
    operation_log, vending_machine = process_operation(operations)
    with open(output_file, 'w') as f:
        f.write(f"{vending_machine['balance']}\n")
        for product, details in vending_machine['products'].items():
            f.write(f"{product} {details['stock']} {details['price']}\n")
    for log in operation_log:
        print(log)

def process_operation(operation: str) -> tuple[list[str], dict]:
    vending_machine = {
        'balance': 0,
        'products': {}
    }
    operation_log = []

    lines = operation.split('\n')
    for line in lines:
        parts = line.split()
        if not parts:
            continue
        oper_code = parts[0]
        
        match oper_code:
            case 'O':
                product = parts[1]
                quantity = int(parts[2])
                money = int(parts[3])
                if product not in vending_machine['products']:
                    operation_log.append(f'{line}: PRODUCT NOT FOUND')
                elif vending_machine['products'][product]['stock'] < quantity:
                    operation_log.append(f'{line}: OUT OF STOCK')
                else:
                    total_price = vending_machine['products'][product]['price'] * quantity
                    if money < total_price:
                        operation_log.append(f'{line}: NOT ENOUGH USER MONEY')
                    else:
                        vending_machine['products'][product]['stock'] -= quantity
                        vending_machine['balance'] += total_price
                        operation_log.append(f'{line}: OK')
            case 'R':
                product = parts[1]
                quantity = int(parts[2])
                if product not in vending_machine['products']:
                    vending_machine['products'][product] = {'price': 1, 'stock': 0}
                vending_machine['products'][product]['stock'] += quantity
                operation_log.append(f'{line}: OK')
            case 'P':
                product = parts[1]
                price = int(parts[2])
                if product not in vending_machine['products']:
                    vending_machine['products'][product] = {'stock': 0, 'price': price}
                else:
                    vending_machine['products'][product]['price'] = price
                operation_log.append(f'{line}: OK')
            case 'M':
                money = int(parts[1])
                vending_machine['balance'] += money
                operation_log.append(f'{line}: OK')
            case _:
                operation_log.append(f'{line}: UNKNOWN OPERATION')

    return operation_log, vending_machine

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
