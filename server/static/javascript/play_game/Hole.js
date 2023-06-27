import React from "react";


export class Hole extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        let style = {
            'backgroundColor': this.props.color,
            'transition': 'background-color 0.2s ease, border 0.2s ease, box-shadow 0.2s ease'
        }
        if (this.props.highlight) {
            style['border'] = '2px solid greenyellow';
            style['boxShadow'] = 'rgba(0, 0, 0, 0.3) 0 20px 36px -20px inset, greenyellow 0 0 10px 0px'
        }

        return (
            <div className="hole" style={style}
                 onClick={(_) => this.props.drop_disc(this.props.column)}
                 onMouseEnter={(_) => this.props.on_mouse_enter(this.props.column)}
                 onMouseLeave={(_) => this.props.on_mouse_leave()}>
            </div>
        )
    }
}