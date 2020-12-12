import React from "react";
import { UserIcon } from "../icons";
import "./User.css";

const User = (props) => (
  <div className="user-message-container">
    <div className="chat-bubble-user">{props.message}</div>
    <div className="img-avatar-container">
      <UserIcon />
    </div>
  </div>
);

export default User;
