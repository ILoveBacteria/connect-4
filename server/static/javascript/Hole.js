import React from "react";


export class Hole extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="hole">{this.props.row}, {this.props.column}</div>
        )
    }
}