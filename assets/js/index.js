import React from 'react'

import Child from './child.js'
import OtherChild from './otherChild.js'

/**
 * Basic example to pass values between parent and child components in React
 * Seems to be in line with this
 * http://stackoverflow.com/questions/24147331/react-the-right-way-to-pass-form-element-state-to-sibling-parent-elements
 * Now I have the state in parent and child. Is that good or bad? Why would I need it in child?
 * Could probably take that out
 * */
class Parent extends React.Component {
  constructor(props) {
    super(props);
    this.onUpdate = this.onUpdate.bind(this);

    this.state = {
      fieldVal: ""
    }
  }

  componentDidMount() {
    var that = this;
    fetch('/api/', {
                method: 'get',
                headers: {'Content-Type':'application/json'}})
            .then((response) => response.json())
            .then((responseData) => {
                this.setState({fieldVal: responseData.text})
            });
  };

  onUpdate(val) {
    this.setState({
      fieldVal: val
    })
  };

  render() {
    return (
      <div>
        <h2>Parent</h2>
        Value in Parent: {this.state.fieldVal}
        <br/>
        <Child onUpdate={this.onUpdate} />
        <br />
        <OtherChild passedVal={this.state.fieldVal} />
      </div>
    )
  }
}

export default Parent