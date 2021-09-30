import React from "react";

const ProjectItem = ({project}) => {
    return (
       <tr>
           <td>
               {project.name}
           </td>
           <td>
               {project.link}
           </td>
           <td>
               {project.users}
           </td>
       </tr>
   )
}

const ProjectList = ({projects}) => {
   return (
       <table className="table">
           <th>
               name
           </th>
           <th>
               link
           </th>
           <th>
               users
           </th>
                {projects.map((map_project) => <ProjectItem project={map_project} />)}
       </table>
   )
}


export default ProjectList
