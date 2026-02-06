import { useState } from "react";

const EnquiryForm = () => {
  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
    destination: "",
    travelType: "",
    startDate: "",
    travelers: "",
    message: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const submitForm = async (e) => {
    e.preventDefault();
    console.log("SUBMITTING FORM:", form);

    try {
      const res = await fetch("/api/enquiries", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      const data = await res.json();

      if (!res.ok) {
        console.error("API ERROR:", data);
        alert("Failed to submit enquiry");
        return;
      }

      alert("🌿 Enquiry saved successfully!");
    } catch (err) {
      console.error("NETWORK ERROR:", err);
      alert("Network error");
    }
  };

  return (
    <form style={styles.form} onSubmit={submitForm}>
      <h2>Travel Enquiry</h2>

      <input name="name" placeholder="Full Name" required onChange={handleChange} />
      <input name="email" placeholder="Email Address" required onChange={handleChange} />
      <input name="phone" placeholder="Phone Number" onChange={handleChange} />

      <select name="destination" required onChange={handleChange}>
        <option value="">Select Destination</option>
        <option>Bali</option>
        <option>Paris</option>
        <option>Switzerland</option>
        <option>Dubai</option>
      </select>

      <select name="travelType" onChange={handleChange}>
        <option>Leisure</option>
        <option>Adventure</option>
        <option>Honeymoon</option>
        <option>Family</option>
      </select>

      <input type="date" name="startDate" onChange={handleChange} />
      <input type="number" name="travelers" placeholder="Number of Travelers" onChange={handleChange} />

      <textarea
        name="message"
        placeholder="Additional requirements or questions"
        rows="4"
        onChange={handleChange}
      />

      {/* THIS IS CRITICAL */}
      <button type="submit" className="btn">
        Submit Enquiry
      </button>
    </form>
  );
};

const styles = {
  form: {
    marginTop: "60px",
    background: "linear-gradient(180deg, #121917, #0c1411)",
    padding: "40px",
    borderRadius: "24px",
    display: "flex",
    flexDirection: "column",
    gap: "15px",
    border: "1px solid rgba(0,255,156,0.2)",
  },
};

export default EnquiryForm;
