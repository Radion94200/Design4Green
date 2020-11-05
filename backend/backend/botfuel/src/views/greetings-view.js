const { View, BotTextMessage } = require('botfuel-dialog');

class GreetingsView extends View {
  render() {
    return [
      new BotTextMessage('Bonjour! Comment puis-je vous aider?'),
    ];
  }
}

module.exports = GreetingsView;
