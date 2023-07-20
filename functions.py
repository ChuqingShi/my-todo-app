FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


def clear_todos(filepath=FILEPATH):
    """ clear everything in the text file. """
    with open(filepath, 'w') as file_local:
        pass


if __name__ == "__main__":
    help(get_todos)
    help(write_todos)
    help(clear_todos)

# print(dir())  # by default, return the names in the current scope(program up to this line).
print("====Module functions is included.====")
