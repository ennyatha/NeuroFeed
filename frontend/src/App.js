import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [topic, setTopic] = useState("");
  const [goal, setGoal] = useState("");
  const [days, setDays] = useState(30);
  const [plan, setPlan] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const generatePlan = async () => {
    if (!topic || !goal) {
      setError("Please fill in both topic and goal.");
      return;
    }
    setError("");
    setLoading(true);
    setPlan(null);
    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/api/studyplans/generate/",
        {
          topic,
          goal,
          duration_days: days,
          user_id: 1,
        }
      );
      setPlan(res.data);
    } catch (err) {
      setError("Something went wrong. Make sure the backend is running.");
    }
    setLoading(false);
  };

  return (
    <div className="app">
      <div className="hero">
        <h1>⚡ NeuroFeed</h1>
        <p className="subtitle">AI-Powered Personalized Study Plans</p>
      </div>

      <div className="card">
        <div className="form-group">
          <label>What do you want to learn?</label>
          <input
            type="text"
            placeholder="e.g. Python Django, Machine Learning, DSA..."
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>What is your goal?</label>
          <input
            type="text"
            placeholder="e.g. Build REST APIs, Get placed at Google..."
            value={goal}
            onChange={(e) => setGoal(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>Duration: {days} days</label>
          <input
            type="range"
            min="7"
            max="90"
            value={days}
            onChange={(e) => setDays(e.target.value)}
          />
          <div className="range-labels">
            <span>7 days</span>
            <span>90 days</span>
          </div>
        </div>

        {error && <div className="error">{error}</div>}

        <button
          className="btn"
          onClick={generatePlan}
          disabled={loading}
        >
          {loading ? "Generating your plan..." : "Generate Study Plan ⚡"}
        </button>
      </div>

      {loading && (
        <div className="loading-card">
          <div className="spinner"></div>
          <p>AI is crafting your personalized study plan...</p>
        </div>
      )}

      {plan && (
        <div className="result-card">
          <div className="result-header">
            <h2>📚 Your {plan.duration_days}-Day Study Plan</h2>
            <div className="tags">
              <span className="tag">{plan.topic}</span>
              <span className="tag">{plan.duration_days} days</span>
            </div>
            <p className="goal-text">Goal: {plan.goal}</p>
          </div>
          <div className="plan-content">
            {plan.plan.split("\n").map((line, i) => {
              if (line.startsWith("**") && line.endsWith("**")) {
                return <h3 key={i}>{line.replace(/\*\*/g, "")}</h3>;
              } else if (line.startsWith("### ")) {
                return <h4 key={i}>{line.replace("### ", "")}</h4>;
              } else if (line.startsWith("* ")) {
                return <li key={i}>{line.replace("* ", "")}</li>;
              } else if (line.startsWith("\t+ ")) {
                return <li key={i} className="sub-li">{line.replace("\t+ ", "")}</li>;
              } else if (line.trim() === "") {
                return <br key={i} />;
              } else {
                return <p key={i}>{line}</p>;
              }
            })}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;