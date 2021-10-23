import React from "react";

const TodoItem = ({todo, deleteToDo}) => {
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
           <td>
                <button onClick={() => deleteToDo(todo.id)}>
                    Delete
                </button>
           </td>
       </tr>
   )
}

const TodoList = ({todos, deleteToDo}) => {
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
                {todos.map((map_todo) => <TodoItem todo={map_todo}
                deleteToDo={deleteToDo}/>)}
       </table>
   )
}


export default TodoList
