import express from "express";
import Enquiry from "../models/Enquiry.js";

const router = express.Router();

router.post("/", async (req, res) => {
  const { name, email, destination } = req.body;

  if (!name || !email || !destination) {
    return res.status(400).json({ error: "Missing required fields" });
  }

  try {
    const enquiry = await Enquiry.create(req.body);
    res.status(201).json(enquiry);
  } catch (err) {
    res.status(500).json({ error: "Failed to create enquiry" });
  }
});

router.get("/", async (req, res) => {
  try {
    const enquiries = await Enquiry.find().sort({ createdAt: -1 });
    res.json(enquiries);
  } catch (err) {
    res.status(500).json({ error: "Failed to fetch enquiries" });
  }
});


export default router;
