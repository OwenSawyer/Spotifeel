import React from 'react'

class Child extends React.Component {
  constructor(props) {
    super(props);
    this.update = this.update.bind(this);
    this.state = {
      fieldVal: ""
    }
  }

  update(e) {
    this.props.onUpdate(e.target.value);
    this.setState({fieldVal: e.target.value});
  };

  render() {
    return (
      <div>
        <h4>Child</h4>
        <input
          type="text"
          placeholder="type here"
          onChange={this.update}
          value={this.state.fieldVal}
        />
      </div>
    )
  }
}

export default Child