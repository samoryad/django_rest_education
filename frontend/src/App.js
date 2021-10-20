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

    deleteProject(name){
        console.log(name)
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

        axios.get('http://127.0.0.1:8000/api/project/', {headers})
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
                this.setState(
                    {
                        'todos': todos.results
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
                                <Link to='/todos'>Todo</Link>
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
                        <Route exact path='/projects' component={() => <ProjectList projects = {this.state.projects} deleteProject = {(name) => this.deleteProject(name)}/>}  />
                        <Route exact path='/todos' component={() => <TodoList todos = {this.state.todos} />}  />
                        <Redirect from='/users' to='/' />
                        <Route exact path='/project/:name' component={() => <ToDoFilteredList todos = {this.state.todos} />}  />
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
