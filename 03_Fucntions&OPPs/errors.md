# Different Types of Error

## Errors in Python

### 1. SyntaxError

```python
    print("Hello')
```

### 2. ZeroDivisionError

```python
    print(10/0)
```

### 3. LogicalError

```python
    def add_val(a,b):
        return a-b
```

### 4. NameError

```python
    Print("Sachin")
```

### 5. IndexError

```python
    lst=[8,7,8,4,5]
    print(lst[9])
```

### 6. ValueError

```python
    print(int('abc'))
```

### 7. TypeError

```python
    print("2" +2)
```

### 8. KeyError

```python
    dct={"Sachin" : 96}
    print(dct["Ram"])
```

### 9. IdentationError

```python
    for i in range(1,6):
    print(i)    
```

### 10. ModuleNotFoundError

```python
    import syssoigh
```

### 11. AttributeError

```python
    x=10
    print(x.upper())
```

### 12. FileNotFoundError

```python
    with open("nonexistent_file.txt", "r") as file:
    content = file.read()

```

### 13. importError

```python
    import nonExitedModule
```

## Exception Handling

### 1. Exception

>> An exception is an error that occurs during the execution of code.
This error causes the code to raise an exception and if not prepared to handle it will halt the execution of the code

```python
    try:
        x=10
        print("x:",x)
        #uncomment the below lines one by one  to understand the working
        # print(x/0) 
        #print(int("3.14"))  
    except ZeroDivisionError as zde:
        print(zde)
        print("ZeroDivisionError Occured")
    except Exception as e:
        print(e)
    else:
        print("This will only run when no error occured in the above try block")
    finally:
        print("This block always execute whether there is error on not")             
```

### 2. Raise Statement

>>When catching exceptions, it's important to consider the context and decide whether to handle the exception locally or raise a new one. The raise statement is useful when you want to propagate an exception with additional information or when you want to replace a caught exception with a more specific one.

```python
    def divide_numbers(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        # You can choose to re-raise the caught exception or raise a different one.
        raise ValueError("Custom error message") from e

    # Example usage:
    try:
        result = divide_numbers(10, 2)
        print(f"Result: {result}")
    except ValueError as ve:
        print(f"Caught a ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"Caught a ZeroDivisionError: {zde}")

```

### 3. Assertion Error

>>Assertions are used to check whether a given logical expression is true or false. If the expression is false, the interpreter will raise an AssertionError exception, and if it's true, the program will continue executing. Assertions are typically used during development and testing to catch potential errors early.

```python
    x = 5
    assert x > 0, "x should be greater than 0"

    name = "John"
    assert len(name) >= 3, "Name should be at least 3 characters long"
```
