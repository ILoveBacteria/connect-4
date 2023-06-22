import React from "react";


export class Hole extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let css_class = ['hole']
        // if (this.props.color == null) {
        //     css_class.push('empty_hole')
        // } else {
        //     css_class.push(`${this.props.color}_hole`)
        // }
        return (
            <div className={css_class.join(' ')}
                 onClick={(e) => this.props.drop_disc(this.props.column)}>
                {this.props.row}, {this.props.column}, {this.props.color}
            </div>
        )
    }
}