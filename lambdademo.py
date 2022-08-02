def printer(message):
    print(f"Vous avez demandé {message}")

def autre_printer(message):
    print(f"Vous avez un nouveaul message: {message}")

def mail_handler(print_message):
    print_message("Hello world")


mail_handler(printer)
mail_handler(autre_printer)
mail_handler(lambda message: print(f"lambda: {message}"))

# lambda <parametres>: <expression>
add = lambda x, y: x + y
print(add(1, 2))