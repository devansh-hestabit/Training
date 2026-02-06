import mongoose from "mongoose";

const enquirySchema = new mongoose.Schema(
  {
    name: { type: String, required: true },
    email: { type: String, required: true },
    phone: String,

    destination: { type: String, required: true },
    travelType: {
      type: String,
      enum: ["Leisure", "Adventure", "Honeymoon", "Family"]
    },

    startDate: Date,
    travelers: Number,
    message: String
  },
  { timestamps: true }
);

export default mongoose.model("Enquiry", enquirySchema);
