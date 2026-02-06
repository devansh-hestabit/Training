import Navbar from "../components/Navbar";
import PackageCard from "../components/PackageCard";
import EnquiryForm from "../components/EnquiryForm";

const Home = () => {
  return (
    <div className="container">
      <Navbar />

      <section style={styles.hero}>
        <h1>
          Discover the World <br />
          <span style={{ color: "#00ff9c" }}>With Confidence</span>
        </h1>
        <p>
          Luxury, adventure, and eco-friendly travel experiences — all in one
          place.
        </p>
        <div style={styles.heroBtns}>
          <button className="btn">Explore Destinations</button>
          <button style={styles.secondaryBtn}>Talk to an Expert</button>
        </div>
      </section>
      <section>
        <h2>Why Choose GreenTrips?</h2>

        <div style={styles.features}>
          <div className="card">🌱 Eco-Friendly Packages</div>
          <div className="card">✈️ Trusted Global Partners</div>
          <div className="card">💬 24/7 Travel Support</div>
          <div className="card">⭐ 5-Star Experiences</div>
        </div>
      </section>

      {/* Packages */}
      <section>
        <h2>Popular Destinations</h2>

        <div style={styles.grid}>
          <PackageCard
            title="Bali, Indonesia"
            price="$1,499"
            desc="Tropical escape."
          />
          <PackageCard
            title="Paris, France"
            price="$2,199"
            desc="Romantic getaway."
          />
          <PackageCard
            title="Swiss Alps"
            price="$2,999"
            desc="Luxury mountain trip."
          />
          <PackageCard
            title="Dubai, UAE"
            price="$1,899"
            desc="Modern luxury."
          />
        </div>
      </section>
      <section>
        <h2>What Our Travelers Say</h2>

        <div style={styles.grid}>
          <div className="card">“Best trip of my life!” ⭐⭐⭐⭐⭐</div>
          <div className="card">
            “Professional and eco-conscious.” ⭐⭐⭐⭐⭐
          </div>
          <div className="card">
            “Amazing service & destinations.” ⭐⭐⭐⭐⭐
          </div>
        </div>
      </section>

      <EnquiryForm />

      <footer style={styles.footer}>
        <p>© 2026 GreenTrips. All rights reserved.</p>
        <p>Built with ❤️ for sustainable travel</p>
      </footer>
    </div>
  );
};

const styles = {
  hero: {
    minHeight: "20vh",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    textAlign: "center",
    gap: "10px",
  },
  heroBtns: {
    display: "flex",
    gap: "20px",
  },
  secondaryBtn: {
    background: "transparent",
    border: "1px solid #00ff9c",
    color: "#00ff9c",
    padding: "12px 24px",
    borderRadius: "30px",
  },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
    gap: "30px",
    marginTop: "60px",
  },
  features: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
    gap: "25px",
    marginTop: "40px",
  },
  footer: {
    marginTop: "120px",
    padding: "40px 0",
    borderTop: "1px solid rgba(0,255,156,0.2)",
    textAlign: "center",
    color: "#9fbfb2",
  },
};

export default Home;
