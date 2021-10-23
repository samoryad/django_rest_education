import React from "react";
import {withRouter} from 'react-router-dom';


class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'project': [],
            'text': '',
            'user': []
        }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleProjectsChange(event) {
        if (!event.target.selectedOptions){
            return
        }
        let project = parseInt(event.target.selectedOptions.item(0).value)

        this.setState({
            'project': project
        })
    }

    handleUsersChange(event) {
        if (!event.target.selectedOptions){
            return
        }
        let user = parseInt(event.target.selectedOptions.item(0).value)

        this.setState({
            'user': user
        })
    }

    handleSubmit(event){
        // console.log(this.state.project, this.state.text, this.state.user)
        this.props.createToDoNotice(this.state.project, this.state.text, this.state.user)
        event.preventDefault()
        this.props.history.push('/todos')
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <select name="project" onChange={(event) => this.handleProjectsChange(event)}>
                    {this.props.projects.map((project) => <option value={project.id}>{project.name}</option>)}
                </select>
                <input type="text" name="text" placeholder="text" value={this.state.text} onChange={(event) => this.handleChange(event)} />
                <select name="user" onChange={(event) => this.handleUsersChange(event)}>
                    {this.props.users.map((user) => <option value={user.id}>{user.username}</option>)}
                </select>
                <input type="submit" value="Create ToDo Notice"/>
            </form>
        );
    }
}

export default withRouter(ToDoForm);
