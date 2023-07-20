import streamlit as st
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass
if not os.path.exists("dones.txt"):
    with open("dones.txt", 'w') as file:
        pass

todos = functions.get_todos()
dones = functions.get_todos("dones.txt")


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    if todo in todos:
        st.warning('You just added an existing todo!', icon="⚠️")
    else:
        todos.append(todo)
        functions.write_todos(todos)
    st.session_state["new_todo"] = ""


def clear_dones():
    for done in dones:
        del st.session_state[done]
    functions.clear_todos("dones.txt")


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")
# st.markdown("""---""")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        dones.append(todo)
        functions.write_todos(dones, "dones.txt")
        del st.session_state[todo]
        st.experimental_rerun()

for index, done in enumerate(dones):
    checkbox = st.checkbox(f"~~{done.strip()}~~", value=True, key=done)
    if not checkbox:
        dones.pop(index)
        functions.write_todos(dones, "dones.txt")
        todos.append(done)
        functions.write_todos(todos)
        del st.session_state[done]
        st.experimental_rerun()

st.text_input(label="Add new todo", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo", label_visibility="collapsed")

st.button("Clear all dones", on_click=clear_dones)
# st.session_state  # for developer use

