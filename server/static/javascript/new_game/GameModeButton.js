import React from "react";


export class GameModeButton extends React.Component {
    render() {
        return (
            <div className="mode-button" onClick={(_) => this.props.on_select(this.props.children)}>
                {this.props.children}
            </div>
        );
    }
}