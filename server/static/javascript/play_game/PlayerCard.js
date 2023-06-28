import React from "react";


export function PlayerCard(props) {
    let style = {
        backgroundColor: props.player.color + '32', // 32 is the opacity
        borderColor: props.player.color,
        transition: 'height 0.2s ease-out',
    }

    if (props.turn || props.winner != null) {
        style['height'] = '7rem';
    }

    let agent_icon = props.player.instance === 'HumanAgent' ? person_icon : ai_icon;

    return (
        <div className="player-card" style={style}>
            <Agent name={props.player.name} turn={props.turn} icon={agent_icon}/>
            <Status spinner={props.turn && props.spinner} winner={props.winner} player={props.player}/>
        </div>
    );
}

function Agent(props) {
    return (
        <div id="agent">
                <span>
                    <span className="agent-icon">{props.icon}</span>
                    <span>{props.name}</span>
                </span>
            <span id="arrow-icon">{props.turn && arrow_icon}</span>
        </div>
    );
}

function Status(props) {
    let win_lose = null;
    if (props.winner != null) {
        let is_win = props.winner.color === props.player.color;
        let style = {color: is_win ? 'hsl(114, 100%, 62%)' : 'hsl(0,100%,62%)'};
        if (is_win) {
            win_lose = <div style={style}><span>{emoji_win}</span><span>Winner</span></div>
        } else {
            win_lose = <div style={style}><span>{emoji_lose}</span><span>Loser</span></div>
        }
    }

    return (
        <div className="status-icon">
            <div className="win-lose-status">{win_lose}</div>
            {props.spinner && <div className="spinner-border" role="status"></div>}
        </div>
    );
}

const SIZE = 26;

let person_icon = (
    <svg xmlns="http://www.w3.org/2000/svg" width={SIZE} height={SIZE} fill="currentColor" className="bi bi-person"
         viewBox="0 0 16 16">
        <path
            d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0Zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4Zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10Z"/>
    </svg>
);

let ai_icon = (
    <svg xmlns="http://www.w3.org/2000/svg" width={SIZE} height={SIZE} fill="currentColor" className="bi bi-robot"
         viewBox="0 0 16 16">
        <path
            d="M6 12.5a.5.5 0 0 1 .5-.5h3a.5.5 0 0 1 0 1h-3a.5.5 0 0 1-.5-.5ZM3 8.062C3 6.76 4.235 5.765 5.53 5.886a26.58 26.58 0 0 0 4.94 0C11.765 5.765 13 6.76 13 8.062v1.157a.933.933 0 0 1-.765.935c-.845.147-2.34.346-4.235.346-1.895 0-3.39-.2-4.235-.346A.933.933 0 0 1 3 9.219V8.062Zm4.542-.827a.25.25 0 0 0-.217.068l-.92.9a24.767 24.767 0 0 1-1.871-.183.25.25 0 0 0-.068.495c.55.076 1.232.149 2.02.193a.25.25 0 0 0 .189-.071l.754-.736.847 1.71a.25.25 0 0 0 .404.062l.932-.97a25.286 25.286 0 0 0 1.922-.188.25.25 0 0 0-.068-.495c-.538.074-1.207.145-1.98.189a.25.25 0 0 0-.166.076l-.754.785-.842-1.7a.25.25 0 0 0-.182-.135Z"/>
        <path
            d="M8.5 1.866a1 1 0 1 0-1 0V3h-2A4.5 4.5 0 0 0 1 7.5V8a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1v1a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-1a1 1 0 0 0 1-1V9a1 1 0 0 0-1-1v-.5A4.5 4.5 0 0 0 10.5 3h-2V1.866ZM14 7.5V13a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V7.5A3.5 3.5 0 0 1 5.5 4h5A3.5 3.5 0 0 1 14 7.5Z"/>
    </svg>
);

let arrow_icon = (
    <svg xmlns="http://www.w3.org/2000/svg" width={SIZE} height={SIZE} fill="currentColor"
         className="bi bi-arrow-left-circle-fill" viewBox="0 0 16 16">
        <path
            d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0zm3.5 7.5a.5.5 0 0 1 0 1H5.707l2.147 2.146a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 1 1 .708.708L5.707 7.5H11.5z"/>
    </svg>
);

let check_icon = (
    <svg xmlns="http://www.w3.org/2000/svg" width={SIZE} height={SIZE} fill="currentColor" className="bi bi-check2"
         viewBox="0 0 16 16">
        <path
            d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"/>
    </svg>
);

let emoji_lose = (
    <svg xmlns="http://www.w3.org/2000/svg" width={SIZE} height={SIZE} fill="currentColor"
         className="bi bi-emoji-dizzy-fill" viewBox="0 0 16 16">
        <path
            d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zM4.146 5.146a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 1 1 .708.708l-.647.646.647.646a.5.5 0 1 1-.708.708L5.5 7.207l-.646.647a.5.5 0 1 1-.708-.708l.647-.646-.647-.646a.5.5 0 0 1 0-.708zm5 0a.5.5 0 0 1 .708 0l.646.647.646-.647a.5.5 0 0 1 .708.708l-.647.646.647.646a.5.5 0 0 1-.708.708l-.646-.647-.646.647a.5.5 0 1 1-.708-.708l.647-.646-.647-.646a.5.5 0 0 1 0-.708zM8 13a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"/>
    </svg>
);

let emoji_win = (
    <svg xmlns="http://www.w3.org/2000/svg" width={SIZE} height={SIZE} fill="currentColor"
         className="bi bi-emoji-smile-fill" viewBox="0 0 16 16">
        <path
            d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zM7 6.5C7 7.328 6.552 8 6 8s-1-.672-1-1.5S5.448 5 6 5s1 .672 1 1.5zM4.285 9.567a.5.5 0 0 1 .683.183A3.498 3.498 0 0 0 8 11.5a3.498 3.498 0 0 0 3.032-1.75.5.5 0 1 1 .866.5A4.498 4.498 0 0 1 8 12.5a4.498 4.498 0 0 1-3.898-2.25.5.5 0 0 1 .183-.683zM10 8c-.552 0-1-.672-1-1.5S9.448 5 10 5s1 .672 1 1.5S10.552 8 10 8z"/>
    </svg>
);