import React, { useState } from "react";

function App() {
  const [role, setRole] = useState("");
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(false);

  const generateQuestions = async () => {
    setLoading(true);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/generate-questions",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            role: role
          })
        }
      );

      const data = await response.json();
      setQuestions(data.questions);
    } catch (error) {
      console.error(error);
      alert("Backend not available");
    }

    setLoading(false);
  };

  return (
    <div
      style={{
        maxWidth: "800px",
        margin: "40px auto",
        padding: "20px"
      }}
    >
      <h1>AI Interview Assistant</h1>

      <input
        type="text"
        placeholder="Enter Role"
        value={role}
        onChange={(e) => setRole(e.target.value)}
        style={{
          width: "100%",
          padding: "10px",
          marginBottom: "15px"
        }}
      />

      <button
        onClick={generateQuestions}
        style={{
          padding: "10px 20px"
        }}
      >
        Generate Questions
      </button>

      {loading && <p>Loading...</p>}

      <ul>
        {questions.map((q, index) => (
          <li key={index}>{q}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;