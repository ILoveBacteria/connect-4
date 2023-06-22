import React from "react";


export class Hole extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let style = {
            'backgroundColor': this.props.color
        }

        return (
            <div className="hole" style={style}
                 onClick={(e) => this.props.drop_disc(this.props.column)}>
                {this.props.row}, {this.props.column}, {this.props.color}
            </div>
        )
    }
}