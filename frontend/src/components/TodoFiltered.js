import React from 'react'
import {useParams} from 'react-router-dom'


const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.created_date}
            </td>
            <td>
                {todo.user}
            </td>
       </tr>
    )
}


const ToDoFilteredList = ({todos}) => {
    let { name } = useParams()
    //TODO не пойму, почему даже консоль.лог не выводит ничего, не разобрался
    //но сидел очень долго. По логике вроде всё верно. может синтаксис
    //не правильный или ещё что-то... объясните пожалуйста
    console.log(name)
    console.log(todos)
    let filtered_todos = todos.filter((todo) => todo.project === name);
    console.log(filtered_todos)

    // return (
    //     <div>Отображается {name}</div>
    // )

    return (
        <table className="table">
            <th>
                project
            </th>
            <th>
                text
            </th>
            <th>
                created_date
            </th>
            <th>
                user
            </th>
                {filtered_todos.map((map_todo) => <TodoItem todo={map_todo} />)}
        </table>
    )
}

export default ToDoFilteredList;
