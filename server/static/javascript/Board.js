import React from "react";
import {Hole} from './Hole'


export class Board extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let holes = []
        for (let i = 5; i >= 0; i--) {
            let row = []
            for (let j = 0; j < 7; j++) {
                row.push(<Hole row={i} column={j}/>)
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