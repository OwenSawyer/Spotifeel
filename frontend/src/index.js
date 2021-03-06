import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import AppRouter, { history } from './routers/AppRouter';
import configureStore from './store/configureStore';
import { startSetExpenses } from './actions/expenses';
import { login, logout } from './actions/auth';
//import getVisibleExpenses from './selectors/expenses';
import './styles/styles.scss';
import 'react-dates/lib/css/_datepicker.css';
import LoadingPage from './components/LoadingPage';

const store = configureStore();
let hasRendered = false;
const renderApp = () => {
    if (!hasRendered) {
        ReactDOM.render((
            <Provider store={store}>
                <AppRouter />
            </Provider>
        ), document.getElementById('root'));
        hasRendered = true;
    }
};

ReactDOM.render(<LoadingPage />, document.getElementById('root'));
store.dispatch(login('abc123'));
store.dispatch(startSetExpenses()).then(() => {
renderApp();
if (history.location.pathname === '/') {
    history.push('/');
}
});
