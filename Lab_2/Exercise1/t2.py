#!/usr/bin/env python3

def print_name(name):
    print_name.called = getattr(print_name, "called", False)
    if not print_name.called:
        print(f"{print_name.__name__} called for First time")
    else:
        print(f"{print_name.__name__} called multiple times")
    print_name.called = True
    print(name)


print_name("Justice")
print_name("Julien")
