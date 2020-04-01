import React, { Component } from 'react'
import { StyleSheet, Switch, View, Text } from 'react-native'

export default class SwitchExample extends Component {
  state = {
    switchValue: false
  };

  render() {
    return (
      <View>
        
      </View>
    );
  }
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  textStyle: {
    margin: 24,
    fontSize: 25,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#344953'
  }
})  