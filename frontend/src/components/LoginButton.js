import React from 'react';
import { connect } from 'react-redux';
//import jsonp from "jsonp";
//import axios from "axios";
// import {
//   spotifyWebApiURL,
//   clientID,
//   redirectURI,
//   clientSecret,
//   spotifyProfileURL
// } from "../../constants";

export class LoginButton extends React.Component {
    constructor(props) {
        super(props);

        this.urlBaseAuth = 'https://accounts.spotify.com/authorize';

        this.state = {
            description: props.expense ? props.expense.description : '',
            note: props.expense ? props.expense.note : '',
            amount: props.expense ? (props.expense.amount / 100).toString() : '',
            //createdAt: props.expense ? moment(props.expense.createdAt) : moment(),
            calendarFocused: false,
            error: ''
        };
    }
    onDescriptionChange = (e) => {
        const description = e.target.value;
        this.setState(() => ({ description }));
    };

    handleAuthFlow = event => {
        event.preventDefault();
        const { clientId, responseType, redirectUri, showDialog, scope, onError } = this.props;

        if (this.state.isAuthenticated) {
            //TODO: refresh token?
        } else {
            //on login: try fetch code from BE (+ refresh), otherwise show login page
            //https://accounts.spotify.com/en/authorize?client_id=xxx&response_type=token&redirect_uri=http://localhost:8888/dashboard
            //redirect to callback?code=xxxx -> send to BE
            let urlAuth = `${this.urlBaseAuth}?client_id=${clientId}&response_type=${responseType}&redirect_uri=${redirectUri}`;

            window.location = urlAuth;
        }
    };

    render() {
        return (
            <div id="login">
                <h1>This is an example of the Authorization Code flow</h1>
                <a href="/login" className="btn btn-primary">Log in with Spotify</a>
            </div>
        )
    }
}

const mapStateToProps = (state) => ({
    responseType: 'token',
    clientId: "",
    authToken: "",
    isAuthenticated: false
});

export default connect(mapStateToProps)(LoginButton);
