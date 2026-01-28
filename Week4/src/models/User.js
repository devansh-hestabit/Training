const mongoose = require("mongoose");
const userSchema = new mongoose.Schema(
  {
    firstName: {
      type: String,
      required: true,
      trim: true,
    },
    lastName: {
      type: String,
      required: true,
      trim: true,
    },
    email: {
      type: String,
      required: true,
      unique: true,
      lowercase: true,
      index: true,
    },
    password: {
      type: String,
      required: true,
      minlength: 6,
    },
    status: {
      type: String,
      enum: ["active", "inactive"],
      default: "active",
    },
  },
  {
    timestamps: true,
  },
);
userSchema.pre("save", async function () {
  if (!this.isModified("password")) return;

  this.password = "hashed_" + this.password;
});

userSchema.virtual("fullName").get(function () {
  return `${this.firstName} ${this.lastName}`;
});
userSchema.index({ status: 1, createdAt: -1 });
module.exports = mongoose.model("User", userSchema);
