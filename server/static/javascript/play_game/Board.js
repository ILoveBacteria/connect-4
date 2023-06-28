import React from "react";
import {Hole} from './Hole'


export class Board extends React.Component {
    constructor(props) {
        super(props);
        this.state = {highlight: [null, null]};
    }

    on_mouse_enter_disc = (column) => {
        for (let i = 0; i < 6; i++) {
            if (this.props.disc_color[i][column] == null) {
                this.setState({highlight: [i, column]});
                break;
            }
        }
    }

    on_mouse_leave_disc = () => {
        this.setState({highlight: [null, null]});
    }

    render() {
        let holes = []
        for (let i = 5; i >= 0; i--) {
            let row = [];
            for (let j = 0; j < 7; j++) {
                let hole = <Hole
                    row={i} column={j} color={this.props.disc_color[i][j]} drop_disc={this.props.drop_disc}
                    highlight={i === this.state.highlight[0] && j === this.state.highlight[1]}
                    on_mouse_enter={this.on_mouse_enter_disc}
                    on_mouse_leave={this.on_mouse_leave_disc}/>
                row.push(hole);
            }
            holes.push(row);
        }

        return (
            <div id="board">{holes}</div>
        )
    }
}