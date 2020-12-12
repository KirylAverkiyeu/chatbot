import React, { useState } from "react";
import Bot from "./Bot";
import User from "./User";
import "./App.css";

function App() {
  const [userMassages, setUserMessages] = useState([]);
  const [botMessages, setBotMessages] = useState([
    "Hi there! My name is ChatBot. You can ask me whatever you want!",
  ]);

  const updateUserMessages = (newMessage) => {
    setUserMessages([...userMassages, newMessage]);

    fetch(`http://localhost:5000/answer/${newMessage}`)
      .then((res) => res.json())
      .then((data) => {
        const botResponse = data.answer;
        // Update state with both user and bot's latest messages
        setBotMessages([...botMessages, botResponse]);
      })
      .catch((error) => console.log(error));
  };

  const handleChange = (event) => {
    if (event.key === "Enter") {
      const userInput = event.target.value;

      updateUserMessages(userInput);
      event.target.value = "";
    }
  };

  const showMessages = () =>
    userMassages.length === 0 ? (
      <Bot message={botMessages[0]} />
    ) : (
      userMassages.map((message, idx) => {
        const botResponse = botMessages[idx + 1];
        return (
          <div key={idx}>
            <User message={message} />
            <Bot message={botResponse} />
          </div>
        );
      })
    );

  return (
    <div className="App">
      {showMessages()}
      <input
        type="text"
        onKeyPress={handleChange}
        placeholder="TYPE IN YOUR QUESTION"
      />
    </div>
  );
}

export default App;
