import React from "react";
import {Hole} from './Hole'


export class Board extends React.Component {
    constructor(props) {
        super(props);
        let discs_color = []
        for (let i = 0; i < 6; i++) {
            let row = []
            for (let j = 0; j < 7; j++) {
                row.push(null)
            }
            discs_color.push(row)
        }
        this.state = {discs_color: discs_color, highlight: [null, null]}
    }

    drop_disc = async (column) => {
        let response = await fetch(`/api/drop_disc/${column}`)
        if (!response.ok) {
            throw 'The response code is not OK!'
        }
        let data = await response.json()
        this.state.discs_color[data.row][data.column] = data.color
        this.setState({})
    }

    on_mouse_enter_disc = (column) => {
        for (let i = 0; i < 6; i++) {
            if (this.state.discs_color[i][column] == null) {
                this.setState({highlight: [i, column]})
                break
            }
        }
    }

    on_mouse_leave_disc = () => {
        this.setState({highlight: [null, null]})
    }

    render() {
        let holes = []
        for (let i = 5; i >= 0; i--) {
            let row = []
            for (let j = 0; j < 7; j++) {
                let hole = <Hole
                    row={i} column={j} color={this.state.discs_color[i][j]} drop_disc={this.drop_disc}
                    highlight={i === this.state.highlight[0] && j === this.state.highlight[1]}
                    on_mouse_enter={this.on_mouse_enter_disc}
                    on_mouse_leave={this.on_mouse_leave_disc}/>
                row.push(hole)
            }
            holes.push(row)
        }

        return (
            <div id="board">
                {holes}
            </div>
        )
    }
}