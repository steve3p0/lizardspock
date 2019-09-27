// src/App.js
import React, {Component} from 'react';
import Languages from './components/languages';

class App extends Component
{
    state = { languages: [] }

    componentDidMount()
    {
        fetch('http://127.0.0.1:5000/language', )
        //fetch('http://jsonplaceholder.typicode.com/users')
            .then(res => res.json())
            .then((data) => { this.setState({ languages: data })})
            .catch(console.log)
      }

    render ()
    {
        return (
            <Languages languages={this.state.languages} />
        );
    }
}

export default App;
