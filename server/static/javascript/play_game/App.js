import React from 'react';
import ReactDOM from 'react-dom';
import {Board} from './Board';
import {PlayerCard} from './PlayerCard';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {mode: null, players: null};
        this.get_game_info();
    }

    get_game_info = async () => {
        let response = await fetch(`/api/game_info`);
        if (!response.ok) {
            throw 'The response code is not OK!';
        }
        let data = await response.json();
        this.setState({mode: data.mode, players: data.players});
    }

    render() {
        return (
            <div>
                <div id="player-cards">
                    {this.state.players && <PlayerCard player={this.state.players[0]}/>}
                    {this.state.players && <PlayerCard player={this.state.players[1]}/>}
                </div>
                <Board mode={this.state.mode}/>
            </div>
        )
    }
}

ReactDOM.render(<App/>, document.getElementById('app'));
