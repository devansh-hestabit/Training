const mongoose = require("mongoose");
const productSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      trim: true,
    },
    price: {
      type: Number,
      required: true,
      min: 0,
    },
    rating: {
      type: Number,
      default: 0,
    },
    status: {
      type: String,
      enum: ["active", "inactive"],
      default: "active",
    },
    deletedAt: {
      type: Date,
      default: null,
    },
  },
  { timestamps: true },
);
productSchema.virtual("ratingLabel").get(function () {
  if (this.rating >= 4) return "Excellent";
  if (this.rating >= 2) return "Average";
  return "Poor";
});
productSchema.index({ status: 1, createdAt: -1 });
module.exports = mongoose.model("Product", productSchema);
