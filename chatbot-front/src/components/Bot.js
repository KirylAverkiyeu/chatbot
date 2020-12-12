import React from "react";

import { BotIcon } from "../icons";
import "./Bot.css";

const Bot = (props) => (
  <div className="bot-message-container">
    <div className="img-avatar-container">
      <BotIcon />
    </div>
    <div className="chat-bubble-bot">{props.message}</div>
  </div>
);

export default Bot;
