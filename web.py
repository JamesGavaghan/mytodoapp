import streamlit as st
import streamlit.errors
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if duplicate_check(todo)==False:
        print("Entered loop")
        todos.append(todo)
        functions.write_todos(todos)
    else:
        print("Nopes")
        st.error("Can not have the same todo twice. Please enter a different todo")
    st.session_state["new_todo"] = ""
def duplicate_check(todotocheck):
    todocheck = False
    for todo in todos:
        if todo == todotocheck:
            todocheck = True
    print(todocheck)
    return todocheck

st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    if todo == "" + "\n":
        break
    else:
       checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        print(todos[index])
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input("Enter a new todo:", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
