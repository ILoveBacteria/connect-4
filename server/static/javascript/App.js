import React from 'react';
import ReactDOM from 'react-dom';
import {Board} from './Board'


class App extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <Board/>
            </div>
        )
    }
}

ReactDOM.render(<App/>, document.getElementById('app'));
