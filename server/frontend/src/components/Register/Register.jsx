import React from "react";

function Register() {
  return (
    <div style={{ maxWidth: "450px", margin: "40px auto", padding: "25px", border: "1px solid #ccc", borderRadius: "10px" }}>
      <h2>Sign Up</h2>
      <form>
        <input type="text" placeholder="Username" required style={inputStyle} />
        <input type="text" placeholder="First Name" required style={inputStyle} />
        <input type="text" placeholder="Last Name" required style={inputStyle} />
        <input type="email" placeholder="Email" required style={inputStyle} />
        <input type="password" placeholder="Password" required style={inputStyle} />
        <button type="submit" style={{ padding: "12px", width: "100%", background: "#007bff", color: "white", border: "none", borderRadius: "5px" }}>Register</button>
      </form>
    </div>
  );
}

const inputStyle = {
  display: "block",
  width: "100%",
  padding: "12px",
  marginBottom: "15px",
  boxSizing: "border-box"
};

export default Register;
