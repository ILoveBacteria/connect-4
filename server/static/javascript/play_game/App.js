import React from 'react';
import ReactDOM from 'react-dom';
import {Board} from './Board';
import {PlayerCard} from './PlayerCard';


class App extends React.Component {
    constructor(props) {
        super(props);
        let disc_color = [];
        for (let i = 0; i < 6; i++) {
            let row = []
            for (let j = 0; j < 7; j++) {
                row.push(null);
            }
            disc_color.push(row);
        }
        this.state = {mode: null, players: null, turn: null, spinner: false, winner: null, disc_color: disc_color};
        this.get_game_info();
    }

    get_game_info = async () => {
        let response = await fetch(`/api/game_info`);
        if (!response.ok) {
            throw 'The response code is not OK!';
        }
        let data = await response.json();
        this.setState({mode: data.mode, players: data.players, turn: data.turn});
    }

    drop_disc = async (column) => {
        this.setState({spinner: true});
        let response = await fetch(`/api/drop_disc/${column}`);
        if (!response.ok) {
            throw 'The response code is not OK!';
        }
        let data = await response.json();
        this.state.disc_color[data.row][data.column] = data.color;
        this.setState({turn: data.turn, spinner: false, winner: data.winner});
    }

    render() {
        return (
            <div>
                <div id="player-cards">
                    {this.state.players && <PlayerCard player={this.state.players[0]} turn={this.state.turn === 0}
                                                       spinner={this.state.spinner} winner={this.state.winner}/>}
                    {this.state.players && <PlayerCard player={this.state.players[1]} turn={this.state.turn === 1}
                                                       spinner={this.state.spinner} winner={this.state.winner}/>}
                </div>
                <Board mode={this.state.mode} disc_color={this.state.disc_color} drop_disc={this.drop_disc}/>
            </div>
        )
    }
}

ReactDOM.render(<App/>, document.getElementById('app'));
