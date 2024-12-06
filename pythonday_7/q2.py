#WAP in python to demonstrate the use of dir () method using module

import math

def demonstrate_dir_with_math_module():
    math_contents = dir(math)
    print("Attributes and methods in the math module:")
    for item in math_contents:
        print(item)
demonstrate_dir_with_math_module()
