// frontend/src/App.js
import React, { useState } from "react";

function App() {
  const [name, setName] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await fetch("https://ai-communicator-bot.onrender.com/create-message/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name }),
    });

    const data = await res.json();
    setResponse(data.message);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Введи ім'я</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Введи ім'я"
          required
        />
        <button type="submit">Від_правити</button>
      </form>
      {response && <p>Відповідь: {response}</p>}
    </div>
  );
}

export default App;
