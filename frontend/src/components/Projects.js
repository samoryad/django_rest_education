import React from "react";
import {Link} from "react-router-dom";

const ProjectItem = ({project, deleteProject}) => {
    return (
       <tr>
           <td>
               {/*{project.name}*/}
               <Link to={`project/${project.name}`}>{project.name}</Link>
           </td>
           <td>
               {project.link}
           </td>
           <td>
               {project.users}
           </td>
           <td>
                <button onClick={() => deleteProject(project.id)}>
                    Delete
                </button>
           </td>
       </tr>
   )
}

const ProjectList = ({projects, deleteProject}) => {
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
                {projects.map((map_project) => <ProjectItem project={map_project}
                deleteProject={deleteProject}/>)}
       </table>
   )
}


export default ProjectList
