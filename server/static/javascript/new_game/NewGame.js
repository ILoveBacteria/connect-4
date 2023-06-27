import React from "react";
import ReactDOM from "react-dom";
import {GameModeButton} from "./GameModeButton";
import {StartButton} from "./StartButton";


class NewGame extends React.Component {
    constructor(props) {
        super(props);
        this.state = {select: null, sending_request: false};
    }

    on_select = (mode) => {
        this.setState({select: mode});
    }

    on_start_click = async () => {
        this.setState({sending_request: true});
        try {
            let response = await fetch(`/game/new_game`, {
                method: 'POST',
                redirect: 'follow',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    mode: this.state.select === '1v1' ? 'multi' : 'single'
                })
            });
            if (response.redirected) {
                window.location.href = response.url;
            }
        } catch (_) {
            this.setState({sending_request: false});
        }
    }

    render() {
        return (
            <div id="form">
                <div id="mode">
                    <GameModeButton on_select={this.on_select} select={this.state.select}>1v1</GameModeButton>
                    <GameModeButton on_select={this.on_select} select={this.state.select}>AI</GameModeButton>
                </div>
                <StartButton disable={this.state.select === null || this.state.sending_request}
                             requesting={this.state.sending_request} on_click={this.on_start_click}/>
            </div>
        );
    }
}

ReactDOM.render(<NewGame/>, document.getElementById('app'));
