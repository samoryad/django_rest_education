import './App.css';
import React from "react";
import UserList from "./components/Users";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        const users =[
            {
        "username": "",
        "first_name": "Ashot",
        "last_name": "Potikyan",
        "email": "Ashot@gb.ru"
        },
            {
        "username": "django",
        "first_name": "",
        "last_name": "",
        "email": "django@gb.ru"
        }
        ]
        this.setState(
            {
                'users': users
            }
        )
    }

    render() {
        return (
            <div>
                <UserList users = {this.state.users}/>
            </div>
        )
    }
}


// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

export default App;
