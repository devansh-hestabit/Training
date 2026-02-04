import React, { useState } from "react";
import { createRoot } from "react-dom/client";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const submit = async (type) => {
    const res = await fetch(`http://localhost:5000/${type}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    const text = await res.text();
    setMessage(text);
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h2>Login System</h2>

        <input
          style={styles.input}
          placeholder="Email"
          onChange={e => setEmail(e.target.value)}
        />

        <input
          style={styles.input}
          type="password"
          placeholder="Password"
          onChange={e => setPassword(e.target.value)}
        />

        <button style={styles.button} onClick={() => submit("register")}>
          Register
        </button>

        <button style={styles.button} onClick={() => submit("login")}>
          Login
        </button>

        <p>{message}</p>
      </div>
    </div>
  );
}

const styles = {
  container: {
    height: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    background: "#f2f2f2"
  },
  card: {
    padding: 30,
    background: "#fff",
    borderRadius: 8,
    width: 300,
    boxShadow: "0 0 10px rgba(0,0,0,0.1)"
  },
  input: {
    width: "100%",
    padding: 10,
    marginBottom: 10
  },
  button: {
    width: "100%",
    padding: 10,
    marginBottom: 10,
    cursor: "pointer"
  }
};

createRoot(document.getElementById("root")).render(<Login />);
