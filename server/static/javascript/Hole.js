import React from "react";


export class Hole extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let class_list = ['hole']
        if (this.props.highlight) {
            class_list.push('hole_hover')
        }
        let style = {
            'backgroundColor': this.props.color
        }

        return (
            <div className={class_list.join(' ')} style={style}
                 onClick={(_) => this.props.drop_disc(this.props.column)}
                 onMouseEnter={(_) => this.props.on_mouse_enter(this.props.column)}
                 onMouseLeave={(_) => this.props.on_mouse_leave()}>
                {this.props.row}, {this.props.column}, {this.props.color}
            </div>
        )
    }
}