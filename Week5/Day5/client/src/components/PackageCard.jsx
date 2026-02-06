const PackageCard = ({ title, price, desc }) => (
  <div style={styles.card}>
    <h3>{title}</h3>
    <p>{desc}</p>
    <strong style={{ color: "#00ff9c" }}>{price}</strong>
  </div>
);


const styles = {
  card: {
    background: "linear-gradient(180deg, #121917, #0c1411)",
    padding: "24px",
    borderRadius: "20px",
    border: "1px solid rgba(0,255,156,0.15)",
    boxShadow: "0 0 30px rgba(0,255,156,0.05)",
    transition: "transform 0.2s ease"
  }
};

export default PackageCard;
