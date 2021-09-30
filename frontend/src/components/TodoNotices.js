import React from "react";

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

const TodoList = ({todos}) => {
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
                {todos.map((map_todo) => <TodoItem todo={map_todo} />)}
       </table>
   )
}


export default TodoList
