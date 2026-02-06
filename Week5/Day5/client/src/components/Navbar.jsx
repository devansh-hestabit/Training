const Navbar = () => {
  return (
    <nav style={styles.nav}>
      <h2 style={styles.logo}>🌍 GreenTrips</h2>
      <div style={styles.links}>
        <a href="#">Home</a>
        <a href="#">Packages</a>
        <a href="#">Enquiry</a>
      </div>
    </nav>
  );
};

const styles = {
  nav: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "20px 0"
  },
  logo: {
    color: "#00ff9c"
  },
  links: {
    display: "flex",
    gap: "20px",
    color: "#9fbfb2"
  }
};

export default Navbar;
