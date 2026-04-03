const mongoose = require("mongoose");
const config = require("../config");
const User = require("../models/User");
const Product = require("../models/Product");

async function seed() {
  try {
    await mongoose.connect(config.mongoUri);
    console.log("MongoDB connected");

    // ---------------- USERS ----------------
    await User.insertMany([
      {
        firstName: "John",
        lastName: "Anderson",
        email: "john.anderson@gmail.com",
        password: "Password@123",
        status: "active",
      },
      {
        firstName: "Emily",
        lastName: "Clark",
        email: "emily.clark@yahoo.com",
        password: "Password@123",
        status: "active",
      },
      {
        firstName: "Michael",
        lastName: "Brown",
        email: "michael.brown@outlook.com",
        password: "Password@123",
        status: "inactive",
      },
      {
        firstName: "Sophia",
        lastName: "Martinez",
        email: "sophia.martinez@gmail.com",
        password: "Password@123",
        status: "active",
      },
      {
        firstName: "David",
        lastName: "Wilson",
        email: "david.wilson@yahoo.com",
        password: "Password@123",
        status: "active",
      },
      {
        firstName: "Olivia",
        lastName: "Taylor",
        email: "olivia.taylor@outlook.com",
        password: "Password@123",
        status: "inactive",
      },
      {
        firstName: "Daniel",
        lastName: "Harris",
        email: "daniel.harris@gmail.com",
        password: "Password@123",
        status: "active",
      },
      {
        firstName: "Emma",
        lastName: "Robinson",
        email: "emma.robinson@yahoo.com",
        password: "Password@123",
        status: "active",
      },
      {
        firstName: "James",
        lastName: "Walker",
        email: "james.walker@gmail.com",
        password: "Password@123",
        status: "inactive",
      },
      {
        firstName: "Ava",
        lastName: "Thompson",
        email: "ava.thompson@outlook.com",
        password: "Password@123",
        status: "active",
      },
    ]);

    console.log("10 users inserted");

    // ---------------- PRODUCTS ----------------
    await Product.insertMany([
      {
        name: "Wireless Noise Cancelling Headphones",
        price: 249,
        rating: 5,
        description:
          "Premium over-ear headphones with active noise cancellation and deep bass.",
      },
      {
        name: "Smart Fitness Watch",
        price: 179,
        rating: 4,
        description:
          "Track your workouts, heart rate, sleep, and daily activity with ease.",
      },
      {
        name: "Ergonomic Office Chair",
        price: 329,
        rating: 5,
        description:
          "Comfortable office chair with lumbar support and breathable mesh design.",
      },
      {
        name: "Portable Bluetooth Speaker",
        price: 89,
        rating: 4,
        description:
          "Compact speaker with powerful sound and long-lasting battery life.",
      },
      {
        name: "Stainless Steel Water Bottle",
        price: 29,
        rating: 4,
        description:
          "Insulated bottle that keeps drinks cold or hot for hours.",
      },
      {
        name: "Mechanical Gaming Keyboard",
        price: 149,
        rating: 5,
        description:
          "RGB backlit mechanical keyboard with tactile switches for gaming.",
      },
      {
        name: "4K Ultra HD Monitor",
        price: 499,
        rating: 5,
        description:
          "High-resolution 27-inch monitor ideal for design and productivity.",
      },
      {
        name: "Wireless Charging Pad",
        price: 39,
        rating: 4,
        description:
          "Fast wireless charging compatible with most modern smartphones.",
      },
      {
        name: "Noise Isolating Earbuds",
        price: 69,
        rating: 3,
        description:
          "In-ear earbuds with clear sound and passive noise isolation.",
      },
      {
        name: "Laptop Backpack",
        price: 79,
        rating: 4,
        description:
          "Durable backpack with padded laptop compartment and multiple pockets.",
      },
    ]);

    console.log("10 products inserted");

    console.log("Seed data inserted successfully");
    process.exit(0);
  } catch (error) {
    console.error("Seeding error:", error);
    process.exit(1);
  }
}

seed();
