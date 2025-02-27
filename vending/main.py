def run(input_file: str, output_file: str) -> None:
    with open(input_file, 'r') as f:
        operations = f.read()

def process_operation(operation: str)-> dict:
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
    #aqui se comprueba se empiezan a procesar las operaciones segun los codigos q vienen recogidos en oper_code
    # vi que tambien se podia hacer esto usando matchcase y seria cambiando el if oper_code de la siguiente manera:
    
    #match oper_code:
        #case 'O':
        if oper_code == 'O':
            product = parts[1]
            quantity = int(parts[2])
            money = int(parts[3])
            #aqui se comprueba si el producto existe
            if product not in vending_machine['products']:
                operation_log.append(f'{line}: PRODUCT NOT FOUND')
                continue
            #aqui si hay stock
            if vending_machine['products'][product]['stock'] < quantity:
                operation_log.append(f'{line}: OUT OF STOCK')
                continue
            total_price = vending_machine['products'][product]['price']
            if money < total_price:
                operation_log.append(f'{line}: NOT ENOUGH USER MONEY')
                continue
            #aqui se resta el stock
            vending_machine['products'][product]['stock'] -= quantity
            #aqui se suma el dinero
            vending_machine['balance'] += total_price
            operation_log.append(f'{line}: OK')

        elif oper_code == 'R':
            product = parts[1]
            quantity = int(parts[2])
            #aqui se comprueba si el producto existe
            if product not in vending_machine['products']:
                operation_log.append(f'{line}: PRODUCT NOT FOUND')
                continue
            #aqui se suma el stock
            vending_machine['products'][product]['stock'] += quantity
            operation_log.append(f'{line}: OK')
        

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
