import React from "react";


export function GameModeButton(props) {
    let style = null;
    if (props.select === props.children) {
        style = {
            backgroundColor: 'rgba(220, 220, 220, 0.3)',
            transition: 'all 0.2s ease',
            boxShadow: 'rgba(220, 220, 220, 0.3) 0 0 10px 8px',
            borderColor: 'rgba(220, 220, 220, 0.85)'
        };
    }

    return (
        <div style={style} className="mode-button" onClick={(_) => props.on_select(props.children)}>
            {props.children}
        </div>
    );
}