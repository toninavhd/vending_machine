def run(input_file: str, output_file: str) -> None:
    # Inicializar la máquina de vending
    machine = {
        "balance": 0,
        "products": {}
    }

    # Procesar cada operación
    with open(input_file, 'r') as f:
        operations = [line.strip() for line in f.readlines()]

    for op_num, operation in enumerate(operations, 1):
        parts = operation.split()
        if not parts:
            print(f"OP{op_num}: E0")
            continue

        op_code = parts[0]
        result = "OK"

        try:
            if op_code == "0":  # Pedir producto
                if len(parts) != 4:
                    result = "E0"
                else:
                    product = parts[1]
                    quantity = int(parts[2])
                    money = int(parts[3])

                    if product not in machine["products"]:
                        result = "E1"
                    else:
                        stock = machine["products"][product]["stock"]
                        price = machine["products"][product]["price"]
                        
                        if stock < quantity:
                            result = "E2"
                        elif money < price * quantity:
                            result = "E3"
                        else:
                            machine["products"][product]["stock"] -= quantity
                            machine["balance"] += price * quantity

            elif op_code == "R":  # Reponer
                if len(parts) != 3:
                    result = "E0"
                else:
                    product = parts[1]
                    quantity = int(parts[2])

                    if product not in machine["products"]:
                        machine["products"][product] = {
                            "stock": 0,
                            "price": 1  # Precio inicial 1€
                        }
                    machine["products"][product]["stock"] += quantity

            elif op_code == "P":  # Cambiar precio
                if len(parts) != 3:
                    result = "E0"
                else:
                    product = parts[1]
                    new_price = int(parts[2])

                    if product not in machine["products"]:
                        result = "E1"
                    else:
                        machine["products"][product]["price"] = new_price

            elif op_code == "M":  # Cargar dinero
                if len(parts) != 2:
                    result = "E0"
                else:
                    amount = int(parts[1])
                    machine["balance"] += amount

            else:  # Operación desconocida
                result = "E0"

        except (ValueError, IndexError):
            result = "E0"

        print(f"OP{op_num}: {result}")

    # Generar archivo de salida
    with open(output_file, 'w') as f:
        f.write(f"{machine['balance']}\n")
        for product in sorted(machine["products"].keys()):
            stock = machine["products"][product]["stock"]
            price = machine["products"][product]["price"]
            f.write(f"{product} {stock} {price}\n")


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    
    vendor.launch(run)
