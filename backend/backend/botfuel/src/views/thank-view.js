const { View, BotTextMessage } = require('botfuel-dialog');

class ThankView extends View {
  render() {
    return [
      new BotTextMessage('De rien!'),
    ];
  }
}

module.exports = ThankView;
