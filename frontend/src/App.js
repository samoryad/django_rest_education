import './App.css';
import React from "react";
import UserList from "./components/Users";
import axios from "axios";
import Header from "./components/Header";
import Footer from "./components/Footer";
import {
    BrowserRouter,
    Link,
    Redirect,
    Route,
    Switch
} from 'react-router-dom';
import ProjectList from "./components/Projects";
import AuthorList from "./components/Authors";
import TodoList from "./components/TodoNotices";
import ToDoFilteredList from "./components/TodoFiltered";
import LoginForm from "./components/LoginForm";
import ProjectForm from "./components/ProjectForm";
import ToDoForm from "./components/ToDoForm";

const NotFound404 = ({ location }) => {
  return (
    <div>
        <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'authors': [],
            'users': [],
            'projects': [],
            'todo': [],
            'token': '',
        }
    }

    getToken(login, password) {
        axios.post(
            'http://127.0.0.1:8000/api-token-auth/',
            {"username": login, "password": password}
        )
            .then(response => {
                localStorage.setItem('token', response.data.token)
                this.setState({'token': response.data.token}, this.loadData)
            })
            .catch(error => alert(error));
    }

    logout() {
        localStorage.setItem('token', '')
        this.setState({'token': ''}, this.loadData)
    }

    isAuthenticated() {
        //преобразовываем к bool и инвертируем
        return !!this.state.token
    }

    getHeaders() {
        if (this.isAuthenticated()) {
            return {'Authorization': 'Token ' + this.state.token}
        }
        return {}
    }

    createProject(name, users) {
        const headers = this.getHeaders()
        // console.log(name, users)
        axios.post('http://127.0.0.1:8000/api/projects/', {name: name, users: users}, {headers})
        .then(response => {
            this.loadData()
        })
        .catch(error => {
            console.log(error)
        })
    }

    deleteProject(id){
        const headers = this.getHeaders()
        // console.log(id)
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}/`, {headers})
        .then(response => {
            this.setState(
                {
                    'projects': this.state.projects.filter((project) => project.id !== id)
                }
            )
        })
        .catch(error => {
            console.log(error)
        })
    }

    createToDoNotice(project, text, user) {
        const headers = this.getHeaders()
        // console.log(project, text, user)
        axios.post('http://127.0.0.1:8000/api/todo/', {project: project, text: text, user: user}, {headers})
        .then(response => {
            this.loadData()
        })
        .catch(error => {
            console.log(error)
        })
    }

    deleteToDo(id){
        const headers = this.getHeaders()
        // console.log(id)
        axios.delete(`http://127.0.0.1:8000/api/todo/${id}/`, {headers})
         .then(response => {
            this.loadData()
        })
        .catch(error => {
            console.log(error)
        })
    }

    loadData(){
        const headers = this.getHeaders()

        axios.get('http://127.0.0.1:8000/api/authors', {headers})
            .then(response => {
                const authors = response.data
                this.setState(
                    {
                        'authors': authors.results
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({
                'authors': []
                })
            })

        axios.get('http://127.0.0.1:8000/api/users', {headers})
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users.results
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({
                'users': []
                })
            })

        axios.get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects.results
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({
                'projects': []
                })
            })

        axios.get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                const todos = response.data
                // console.log(todos)
                this.setState(
                    {
                        'todos': todos.results.filter((todo) => todo.is_active !== false)
                    }
                )
            })
            .catch(error => {
                console.log(error)
                this.setState({
                'todos': []
                })
            })
    }

    componentDidMount() {
        const token = localStorage.getItem('token')
        this.setState({'token': token}, this.loadData)
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <Header/>
                    <nav className="nav">
                        <ul>
                            <li>
                                <Link to='/authors'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/project/create'>Create Project</Link>
                            </li>
                            <li>
                                <Link to='/todos'>Todo</Link>
                            </li>
                            <li>
                                <Link to='/todo/create'>Create Notice</Link>
                            </li>
                            <li>
                                { this.isAuthenticated() ?
                                    <button onClick={()=>this.logout()}>Logout</button> :
                                    <Link to='/login'>Login</Link>
                                }
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/authors' component={() => <AuthorList authors= {this.state.users} />}  />
                        <Route exact path='/' component={() => <UserList users = {this.state.users} />}  />
                        <Route exact path='/projects' component={() => <ProjectList projects = {this.state.projects} deleteProject = {(id) => this.deleteProject(id)}/>}  />
                        <Route exact path='/project/create' component={() => <ProjectForm users = {this.state.users} createProject = {(name, users) => this.createProject(name, users)}/>}  />
                        <Route exact path='/todos' component={() => <TodoList todos = {this.state.todos} deleteToDo = {(id) => this.deleteToDo(id)}/>}  />
                        <Route exact path='/todo/create' component={() => <ToDoForm projects = {this.state.projects} users = {this.state.users} createToDoNotice = {(project, text, user) => this.createToDoNotice(project, text, user)}/>}  />
                        <Redirect from='/users' to='/' />
                        <Route exact path='/project/:id' component={() => <ToDoFilteredList todos = {this.state.todos} />}  />
                        <Route path='/login' component={() => <LoginForm getToken={(login, password) => this.getToken(login, password)} />} />
                        <Route component={NotFound404} />
                        {/*<UserList users = {this.state.users}/>*/}
                    </Switch>
                    <Footer/>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
