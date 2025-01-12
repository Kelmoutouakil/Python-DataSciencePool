def NULL_not_found(object:any) -> int:
    match object:
        case None:
            print("Nothing: None ",type(object))
        case float() if object != object:
            print("Cheese: nan <class 'float'>$")
        case bool():
            print("Fake: False <class 'bool'>$")
        case int() if object == 0:
            print("Zero: 0 ",type(object))
        case str() if object == '':
            print("Empty: <class 'str'>$")
        case _ :
            print("Type not Found")
            return(1)
    return 0

