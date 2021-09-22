import React from "react";

const UserItem = ({user}) => {
    return (
       <tr>
           <td>
               {user.first_name}
           </td>
           <td>
               {user.last_name}
           </td>
           <td>
               {user.email}
           </td>
       </tr>
   )
}

const UserList = ({users}) => {
   return (
       <table className="table">
           <th>
               first_name
           </th>
           <th>
               last_name
           </th>
           <th>
               birthday_year
           </th>
           {users.map((map_user) => <UserItem user={map_user} />)}
       </table>
   )
}


export default UserList
