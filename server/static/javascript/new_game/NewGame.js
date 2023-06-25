import React from "react";
import ReactDOM from "react-dom";
import {GameModeButton} from "./GameModeButton";
import {StartButton} from "./StartButton";


class NewGame extends React.Component {
    constructor(props) {
        super(props);
        this.state = {'select': null}
    }

    on_select = (mode) => {
        this.setState({'select': mode})
    }

    on_start_click = async () => {
        let response = await fetch(`/game/new_game`, {
            method: 'POST',
            redirect: 'follow',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                mode: this.state.select === '1v1' ? 'multi' : 'single'
            })
        })
        if (response.redirected) {
            window.location.href = response.url;
        }
    }

    render() {
        return (
            <div id="form">
                <div id="mode">
                    <GameModeButton on_select={this.on_select} select={this.state.select}>1v1</GameModeButton>
                    <GameModeButton on_select={this.on_select} select={this.state.select}>AI</GameModeButton>
                </div>
                <StartButton disable={this.state.select === null} on_click={this.on_start_click}/>
            </div>
        );
    }
}

ReactDOM.render(<NewGame/>, document.getElementById('app'));
