import React from 'react'

class OtherChild extends React.Component {
  render() {
    return (
      <div>
        <h4>Other Child</h4>
        Value in Other Child Props: {this.props.passedVal}
      </div>
    )
  }
}

export default OtherChild