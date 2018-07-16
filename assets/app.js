import React from 'react'
import ReactDOM from 'react-dom'
import { AppContainer } from 'react-hot-loader'
import Parent from './js/index'

const render = Component => {
  ReactDOM.render(
    <AppContainer>
      <Component />
    </AppContainer>,
    document.getElementById('container'),
  )
}

render(Parent)

// Webpack Hot Module Replacement API
if (module.hot) {
  module.hot.accept('./js/index', () => {
    render(Parent)
  })
}
//
// ReactDOM.render(<Parent/>, document.getElementById('container'));

// ReactDOM.render(
//   <AppContainer>
//     <Parent/>
//   </AppContainer>,
//   document.getElementById('container')
// );
//
// // Hot Module Replacement API
// if (module.hot) {
//   module.hot.accept('./js/index', () => {
//     const NextApp = require('./js/index').default;
//     ReactDOM.render(
//       <AppContainer>
//         <NextApp/>
//       </AppContainer>,
//       document.getElementById('container')
//     );
//   });
// }