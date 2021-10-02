import './App.css';
import React from "react";
import UserList from "./components/Users";
import axios from "axios";
import Header from "./components/Header";
import Footer from "./components/Footer";
import {
    BrowserRouter,
    // HashRouter,
    Link,
    Redirect,
    Route,
    Switch
} from 'react-router-dom';
import ProjectList from "./components/Projects";
import TodoList from "./components/TodoNotices";
import ToDoFilteredList from "./components/TodoFiltered";

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
            'users': [],
            'projects': [],
            'todo': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users')
            .then(response => {
                const users = response.data
                this.setState(
                    {
                        'users': users.results
                    }
                )
            })
            .catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/project/')
            .then(response => {
                const projects = response.data
                this.setState(
                    {
                        'projects': projects.results
                    }
                )
            })
            .catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const todos = response.data
                this.setState(
                    {
                        'todos': todos.results
                    }
                )
            })
            .catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <Header/>
                    <nav className="nav">
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/todos'>Todo</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users = {this.state.users} />}  />
                        <Route exact path='/projects' component={() => <ProjectList projects = {this.state.projects} />}  />
                        <Route exact path='/todos' component={() => <TodoList todos = {this.state.todos} />}  />
                        <Redirect from='/users' to='/' />
                        <Route exact path='/projects/:name' component={() => <ToDoFilteredList todos = {this.state.todos} />}  />
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
