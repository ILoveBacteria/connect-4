import React from "react";


export class StartButton extends React.Component {
    render() {
        let class_ = ['btn', 'btn-primary', 'btn-lg'];
        if (this.props.disable) {
            class_.push('disabled');
        }
        if (this.props.requesting) {
            return (
                <button className={class_.join(' ')} type="button">
                    <span className="spinner-border spinner-border-sm" role="status"></span>
                    <span style={{marginLeft: '0.5rem'}}>Starting Game...</span>
                </button>
            );
        }
        return <button type="button" className={class_.join(' ')}
                       onClick={(_) => this.props.on_click()}>Start</button>
    }
}