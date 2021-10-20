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
    let { id } = useParams()
    // console.log(id)
    // console.log(todos)
    let filtered_todos = todos.filter((todo) => todo.project.id === id);
    // console.log(filtered_todos)

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
