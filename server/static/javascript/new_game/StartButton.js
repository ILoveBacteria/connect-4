import React from "react";


export class StartButton extends React.Component {
    render() {
        let class_ = ['btn', 'btn-primary', 'btn-lg']
        if (this.props.disable) {
            class_.push('disabled')
        }
        return <button type="button" className={class_.join(' ')}
                       onClick={(_) => this.props.on_click()}>Start</button>
    }
}